import re
from typing import Optional, Tuple, List
from .config import NUMBER_WORDS

def normalize_spaces(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def parse_number(text: str) -> Optional[int]:
    if not text:
        return None

    t = (text.lower()
         .replace(',', '')
         .replace('rupees', '')
         .replace('₹', '')
         .replace('rs', '')
         .replace('only', '')
         .replace('रुपये', '')
         .strip())

    if t.isdigit():
        return int(t)

    if '.' in t:
        t = t.split('.')[0]

    tokens = re.findall(r"[a-zA-Z]+|[\u0900-\u097F]+|\d+", t)

    total = 0
    current = 0

    for token in tokens:
        if token.isdigit():
            current += int(token)
            continue

        if token not in NUMBER_WORDS:
            continue

        val = NUMBER_WORDS[token]

        if val >= 100:
            if current == 0:
                current = 1
            current *= val
            total += current
            current = 0
        else:
            current += val

    total += current
    return total if total >= 1 else None


def expand_double_triple(words: List[str]) -> List[str]:
    out = []
    i = 0
    while i < len(words):
        w = words[i]
        if w in ("double", "triple", "दोहरा", "तीन") and i + 1 < len(words):
            count = 2 if w in ("double", "दोहरा") else 3
            out.extend([words[i + 1]] * count)
            i += 2
        else:
            out.append(w)
            i += 1
    return out


def parse_pincode_and_clean(text: str) -> Tuple[Optional[str], str]:
    original = normalize_spaces(text)
    lower = original.lower()

    # Direct digits
    m = re.search(r"\b(\d{6})\b", lower)
    if m:
        pin = m.group(1)
        cleaned = normalize_spaces(re.sub(r"\b\d{6}\b", "", original))
        cleaned = re.sub(r"(pin|code|पिन|कोड)\s*:?", "", cleaned, flags=re.I)
        return pin, cleaned.strip(" ,")

    # Spoken
    words = re.split(r"\s+", lower)
    words = expand_double_triple(words)

    for start in range(len(words) - 5):
        chunk = words[start:start+6]
        digits = []
        if all(w in NUMBER_WORDS and 0 <= NUMBER_WORDS[w] <= 9 for w in chunk):
            digits = [str(NUMBER_WORDS[w]) for w in chunk]
            pin = "".join(digits)
            cleaned = normalize_spaces(" ".join(words[:start] + words[start+6:]))
            cleaned = re.sub(r"(pin|code|पिन|कोड)\s*:?", "", cleaned, flags=re.I)
            return pin, cleaned.strip(" ,")

    return None, original.strip(" ,")
