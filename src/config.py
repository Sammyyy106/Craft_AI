from typing import Dict, List

NUMBER_WORDS: Dict[str, int] = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
    "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
    "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13,
    "hundred": 100, "thousand": 1000, "lakh": 100000, "lac": 100000,
    "crore": 10000000,
    "ek": 1, "do": 2, "teen": 3, "chaar": 4, "paanch": 5,
    "chhah": 6, "saat": 7, "aath": 8, "nau": 9, "dus": 10,
    "hazaar": 1000, "sau": 100,
    "एक": 1, "दो": 2, "तीन": 3, "चार": 4, "पांच": 5,
    "छह": 6, "सात": 7, "आठ": 8, "नौ": 9, "दस": 10,
    "लाख": 100000, "हजार": 1000,
}

LOAN_TYPES = {
    "home": "home", "होम": "home", "घर": "home", "गृह": "home",
    "personal": "personal", "पर्सनल": "personal",
    "vehicle": "vehicle", "वाहन": "vehicle", "car": "vehicle",
    "gold": "gold", "सोना": "gold",
}

INCOME_SOURCES = {
    "salaried": "salaried", "salary": "salaried", "वेतनभोगी": "salaried",
    "self employed": "self_employed", "self-employed": "self_employed",
    "स्वरोजगार": "self_employed", "sarojgar": "self_employed",
    "saroj gar": "self_employed", "svarojgar": "self_employed",
    "business": "self_employed",
}

LOAN_QUESTION_PATTERNS = [
    r"किस.*(लोन|ऋण|loan).*चाहि?",
    r"कौन.*(प्रकार|तरह).*लोन",
    r"क्या.*लोन.*चाह",
    r"which.*loan", r"what.*kind.*loan"
]

INCOME_QUESTION_PATTERNS = [
    r"मासिक.*आय", r"monthly.*income", r"कितनी.*कमाई"
]

SOURCE_QUESTION_PATTERNS = [
    r"(वेतनभोगी|स्वरोजगार|salary|self.*employed)",
    r"आय.*स्रोत", r"income.*source"
]

ADDRESS_QUESTION_PATTERNS = [
    r"(पता|address).*(पिन|pin)",
    r"पिन.*कोड", r"where.*live|residence|address"
]
