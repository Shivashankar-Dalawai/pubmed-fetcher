import logging

def setup_logger(debug: bool = False):
    level = logging.DEBUG if debug else logging.INFO
    logging.basicConfig(level=level, format="%(levelname)s: %(message)s")

def normalize_text(text: str) -> str:
    return text.strip().lower()
