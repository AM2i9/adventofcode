import os
from pathlib import Path
from functools import wraps

import requests

try:
    import dotenv
    dotenv.load_dotenv()
except ImportError:
    pass

BASE_URL = "https://adventofcode.com/"

session = requests.Session()
session.cookies.update({"session": os.getenv("SESSION")})

def getch_input(year, day):
    path = Path(f"inputs/{year}/{day}.txt")
    if path.exists():
        return path.read_text()
    else:
        text = fetch_input(year, day)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)
        return text

def fetch_input(year, day):
    """
    Fetch raw input for an AoC challenge from the website
    """
    req = session.get(BASE_URL + f"{year}/day/{day}/input")
    req.raise_for_status()
    return req.text

def aoc(year, day):
    def wrapper(func):
        return func(getch_input(year, day))
    return wrapper