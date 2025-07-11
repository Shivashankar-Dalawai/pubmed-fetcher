import re

PHARMA_KEYWORDS = ['pharma', 'biotech', 'therapeutics', 'laboratories', 'inc', 'llc', 'gmbh']

def is_pharma_affiliation(text: str) -> bool:
    text = text.lower()
    if any(word in text for word in PHARMA_KEYWORDS) and not any(x in text for x in ["university", "college", "institute"]):
        return True
    return False

def extract_emails(text: str) -> list:
    return re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)
