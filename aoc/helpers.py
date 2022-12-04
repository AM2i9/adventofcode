import os
import re
import traceback
import datetime
import time
import importlib
from pathlib import Path
from functools import wraps

import dateparser
from tqdm import tqdm
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

def _check_answer_cache(year, day, part, answer):
    path = Path(f"{CACHE}/answers/{year}/{day}-{part}.txt")

    if not path.exists():
        return False

    with open(path, "r") as f:
        if f'{answer}' in f.read().splitlines():
            return True
    return False

def _cache_wrong_answer(year, day, part, answer):
    path = Path(f"{CACHE}/answers/{year}/{day}-{part}.txt")

    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.touch()

    with open(path, "a") as f:
        f.write(f"{answer}\n")

def submit(year, day, part, answer):
    if _check_answer_cache(year, day, part, answer):
        print("Answer incorrect (cached)")
        return

    if not os.getenv("SESSION"):
        raise RuntimeError("No session token provided. Cannot submit answer.")

    req = session.post(BASE_URL + f"{year}/day/{day}/answer", data={"level": part, "answer": answer})
    req.raise_for_status()

    msg = re.findall("<article>(.*)<\/article>", req.text, re.S)[0].strip("<p>")

    if "You gave" in msg:
        print("Ratelimited, waiting...")
        timestr = re.findall("You have (.*?) left to wait.", msg)[0]
        sec = (datetime.datetime.now() - dateparser.parse(timestr)).seconds

        for _ in tqdm(range(sec)):
            time.sleep(1)
        print("Ratelimit ended")
        return submit(year, day, part, answer)
    elif "That's the" in msg:
        print("Correct!!!")
    else:
        print("Wrong answer")
        _cache_wrong_answer(year, day, part, answer)
        print(msg)
        

def run_tests(year, day, part=None):
    print(f"Runing solutions for Day {day} ({year})...")
    results = []
    for i in range(1, 3) if part is None else [part]:

        try:
            sol = importlib.import_module(f'{year}.{day:>02}')
            if sol:
                res = getattr(sol, f"part{i}")()
                results.append(res)
                print(f"Part {i} result:", res)
            else:
                print(f"Unable to import module '{year}.{day:>02}'")
        except Exception as e:
            print(f"Part {1} failed with exception:")
            traceback.print_exception(e)

    return tuple(results)

def aoc(year, day):
    def wrapper(func):
        def _wrapped():
            return func(getch_input(year, day))
        return _wrapped
    return wrapper