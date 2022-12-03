import os
import traceback
import timeit
import importlib
from pathlib import Path
from functools import wraps

import requests

try:
    import dotenv
    dotenv.load_dotenv()
except ImportError:
    pass

USER_AGENT = "https://github.com/AM2i9/adventofcode"
BASE_URL = "https://adventofcode.com/"
CACHE = ".aoc"

session = requests.Session()
session.cookies.update({"session": os.getenv("SESSION")})
session.headers.update({"User-Agent": USER_AGENT})

def getch_input(year, day):
    path = Path(f"{CACHE}/inputs/{year}/{day}.txt")
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
    if not os.getenv("SESSION"):
        raise RuntimeError("No session token provided. Cannot fetch input.")
    req = session.get(BASE_URL + f"{year}/day/{day}/input")
    req.raise_for_status()
    return req.text

def submit(year, day, part, answer):
    if not os.getenv("SESSION"):
        raise RuntimeError("No session token provided. Cannot fetch input.")
    req = session.post(BASE_URL + f"{year}/day/{day}/answer",
                        json={"level": part, "answer": answer})
    req.raise_for_status()
    if "That's the right answer!" in req.text:
        print("Answer correct!")
    else:
        print("Answer incorrect.")

def run_tests(year, day, part=None):
    print(f"Runing solutions for Day {day} ({year})...")
    
    for i in range(1, 3) if part is None else [part]:
        try:
            sol = importlib.import_module(f'solutions.{day:>02}')
            if sol:
                time = timeit.timeit(lambda: print(f"Part {i} result:", getattr(sol, f"part{i}")(), end=" "), number=1)
                print(f"({time:.5f} ms)")
            else:
                print(f"Unable to import module 'solutions.{day:>02}'")
        except Exception as e:
            print(f"Part {1} failed with exception:")
            traceback.print_exception(e)

def aoc(year, day):
    def wrapper(func):
        def _wrapped():
            return func(getch_input(year, day))
        return _wrapped
    return wrapper