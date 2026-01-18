import re
from typing import Dict, Optional, Union
from .config import (
    LOAN_QUESTION_PATTERNS, INCOME_QUESTION_PATTERNS,
    SOURCE_QUESTION_PATTERNS, ADDRESS_QUESTION_PATTERNS,
    LOAN_TYPES, INCOME_SOURCES
)
from .parsers import parse_number, parse_pincode_and_clean, normalize_spaces


def is_question_about(text: str, patterns: list) -> bool:
    t = text.lower()
    return any(re.search(p, t) for p in patterns)


def normalize_loan_type(text: str) -> str:
    t = normalize_spaces(text.lower().replace("loan", "").replace("लोन", "").replace("ऋण", ""))
    for k, v in LOAN_TYPES.items():
        if k in t:
            return v
    return ""


def normalize_income_source(text: str) -> str:
    t = normalize_spaces(text.lower())
    for k, v in INCOME_SOURCES.items():
        if k in t:
            return v
    return ""


def is_negative_response(text: str) -> bool:
    """Check if text is a negative response like 'no', 'नहीं', etc."""
    if not text:
        return False
    t = normalize_spaces(text.lower().strip())
    negative_patterns = [
        "नहीं", "nahi", "no", "nope", "none", "na", "nhi",
        "न", "कुछ नहीं", "nothing", "not provided", "not available"
    ]
    return t in negative_patterns or any(t == pattern for pattern in negative_patterns)


def extract_from_transcript(transcript: str, debug: bool = False) -> Dict[str, Union[str, int, bool]]:
    lines = [line.strip() for line in transcript.split("\n") if line.strip()]
    turns = []

    for line in lines:
        lower = line.lower()
        if lower.startswith("assistant:"):
            turns.append(("assistant", line.split(":", 1)[1].strip()))
        elif lower.startswith("user:"):
            turns.append(("user", line.split(":", 1)[1].strip()))

    result = {
        "loan_type": "",
        "monthly_income": None,
        "source_of_income": "",
        "address": "",
        "pincode": ""
    }

    i = 0
    while i < len(turns):
        speaker, text = turns[i]
        if speaker == "assistant":
            if debug and any(p in text.lower() for p in ["लोन", "loan", "आय", "income", "पता", "pin"]):
                print(f"[DEBUG] Question detected → {text[:70]}...")

            if is_question_about(text, LOAN_QUESTION_PATTERNS):
                if i+1 < len(turns) and turns[i+1][0] == "user":
                    result["loan_type"] = normalize_loan_type(turns[i+1][1])

            elif is_question_about(text, INCOME_QUESTION_PATTERNS):
                if i+1 < len(turns) and turns[i+1][0] == "user":
                    inc = parse_number(turns[i+1][1])
                    if inc is not None:
                        result["monthly_income"] = inc

            elif is_question_about(text, SOURCE_QUESTION_PATTERNS):
                if i+1 < len(turns) and turns[i+1][0] == "user":
                    src = normalize_income_source(turns[i+1][1])
                    if src:
                        result["source_of_income"] = src

            elif is_question_about(text, ADDRESS_QUESTION_PATTERNS):
                if i+1 < len(turns) and turns[i+1][0] == "user":
                    pin, cleaned = parse_pincode_and_clean(turns[i+1][1])
                    if pin:
                        result["pincode"] = pin
                    if cleaned and not is_negative_response(cleaned):
                        result["address"] = cleaned

        i += 1

    # Fallbacks
    all_user_text = " ".join(t[1] for t in turns if t[0] == "user")

    if not result["loan_type"]:
        result["loan_type"] = normalize_loan_type(all_user_text)

    if result["monthly_income"] is None:
        inc = parse_number(all_user_text)
        if inc:
            result["monthly_income"] = inc

    if not result["source_of_income"]:
        src = normalize_income_source(all_user_text)
        if src:
            result["source_of_income"] = src

    # Prefer recent messages for address
    if not result["address"] or not result["pincode"]:
        user_msgs = [t[1] for t in turns if t[0] == "user"]
        recent = " ".join(user_msgs[-2:]) if len(user_msgs) >= 2 else user_msgs[-1] if user_msgs else ""
        if recent:
            pin, cleaned = parse_pincode_and_clean(recent)
            if pin and not result["pincode"]:
                result["pincode"] = pin
            if cleaned and not result["address"] and not is_negative_response(cleaned):
                result["address"] = cleaned

    # Final check: if address is a negative response, make it empty
    final_address = result["address"]
    if is_negative_response(final_address):
        final_address = ""
    
    # Build final result with JSON structure (keep address and pincode separate)
    output = {
        "loan_type": result["loan_type"] or "",
        "monthly_income": result["monthly_income"],
        "source_of_income": result["source_of_income"] or "",
        "address": final_address or "",
        "pincode": result["pincode"] or "",
        "interested": True
    }

    return output
