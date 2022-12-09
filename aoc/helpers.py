import os
import re
import traceback
import datetime
import time
import importlib
from pathlib import Path
from functools import wraps

from colorama import Fore, Style
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
        raise RuntimeError(
            f"🎅 {Fore.YELLOW}No session token provided. Cannot submit answer.{Style.RESET_ALL}"
        )
    req = session.get(BASE_URL + f"{year}/day/{day}/input")
    req.raise_for_status()
    return req.text


def _check_wrong_answer_cache(year, day, part, answer):
    path = Path(f"{CACHE}/answers/{year}/{day}-{part}.txt")

    if not path.exists():
        return False

    with open(path, "r") as f:
        if f"{answer}" in f.read().splitlines():
            return True
    return False


def _check_right_answer_cache(year, day, part, answer):
    path = Path(f"{CACHE}/answers/{year}/{day}-{part}.solution.txt")

    if not path.exists():
        return False

    with open(path, "r") as f:
        return f.read() == f"{answer}"


def _cache_right_answer(year, day, part, answer):
    path = Path(f"{CACHE}/answers/{year}/{day}-{part}.solution.txt")

    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.touch()

    with open(path, "w") as f:
        f.write(f"{answer}\n")


def _cache_wrong_answer(year, day, part, answer):
    path = Path(f"{CACHE}/answers/{year}/{day}-{part}.txt")

    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.touch()

    with open(path, "a") as f:
        f.write(f"{answer}\n")


def submit(year, day, part, answer):
    if _check_wrong_answer_cache(year, day, part, answer):
        if (
            input(
                f"{Fore.YELLOW}You have wrong answers. Submit anyway? y/N{Style.RESET_ALL}"
            ).upper()
            != "Y"
        ):
            return
    elif _check_right_answer_cache(year, day, part, answer):
        if (
            input(
                f"{Fore.YELLOW}You have already solved this puzzle. Submit anyway? y/N{Style.RESET_ALL}"
            ).upper()
            != "Y"
        ):
            return
    else:
        print(
            f"Submitting the following value for part {part}: {Fore.YELLOW}{answer} {Style.RESET_ALL}"
        )
        if not input(f"{Fore.GREEN}Confirm? Y/n{Style.RESET_ALL}").upper() in ("Y", ""):
            return

    if not os.getenv("SESSION"):
        raise RuntimeError(
            f"🎅 {Fore.YELLOW}No session token provided. Cannot submit answer.{Style.RESET_ALL}"
        )

    req = session.post(
        BASE_URL + f"{year}/day/{day}/answer", data={"level": part, "answer": answer}
    )
    req.raise_for_status()

    msg = re.findall("<article>(.*)<\/article>", req.text, re.S)[0].strip("<p>")

    if "You gave" in msg:
        print(f"🕑 {Fore.YELLOW}Ratelimited, waiting...{Style.RESET_ALL}")
        timestr = re.findall("You have (.*?) left to wait.", msg)[0]
        sec = (datetime.datetime.now() - dateparser.parse(timestr)).seconds

        for _ in tqdm(range(sec)):
            time.sleep(1)
        print(f"🔔 {Fore.GREEN}Ratelimit ended{Style.RESET_ALL}")
        return submit(year, day, part, answer)
    elif "That's the" in msg:
        print(f"🌟 {Fore.GREEN}Answer Correct!!!{Style.RESET_ALL}")
        _cache_right_answer(year, day, part, answer)
    elif "You don't seem" in msg:
        print(f"🌟 {Fore.GREEN}You've already solved this puzzle.{Style.RESET_ALL}")
    else:
        print(f"❌ {Fore.RED}Wrong answer{Style.RESET_ALL}")
        _cache_wrong_answer(year, day, part, answer)
        print(msg)


def run_tests(year, day, part=None):
    print(f"🎄{Fore.GREEN} Runing solutions for Day {day} ({year})...{Style.RESET_ALL}")
    results = []
    for i in range(1, 3) if part is None else [part]:
        try:
            sol = importlib.import_module(f"{year}.{day:>02}")
            if sol:
                res = getattr(sol, f"part{i}")()
                results.append(res)
                m = ""
                if _check_right_answer_cache(year, day, i, res):
                    m = f" 🎄 {Fore.GREEN}Correct (cached){Style.RESET_ALL}"
                elif _check_wrong_answer_cache(year, day, i, res):
                    m = f" ❌ {Fore.RED}Wrong answer (cached){Style.RESET_ALL}"
                print(
                    f"🎁 Part {Fore.YELLOW}{i}{Style.RESET_ALL} result: {Fore.YELLOW}{res}{Style.RESET_ALL}{m}"
                )
            else:
                print(
                    f"{Fore.RED}Unable to import module '{year}.{day:>02}'{Style.RESET_ALL}"
                )
        except Exception as e:
            print(f"{Fore.RED}Part {1} failed with exception:{Style.RESET_ALL}")
            traceback.print_exception(e)

    return tuple(results)


def aoc(year, day):
    def wrapper(func):
        def _wrapped():
            return func(getch_input(year, day))

        return _wrapped

    return wrapper
