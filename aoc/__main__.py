import argparse
import webbrowser
from datetime import date
from pathlib import Path

from aoc.helpers import run_tests, submit

parser = argparse.ArgumentParser(
    prog = "AoC Helper",
    description = "Helper program for Advent of Code",
)

today = date.today()

parser.add_argument("--test", action='store_true')
parser.add_argument("--submit", action='store_true')

parser.add_argument("--year", type=int, default=today.year)
parser.add_argument("--day", type=int, default=today.day)
parser.add_argument("--part", type=int, default=None)

args = parser.parse_args()

path = Path(f"{args.year}/{args.day:>02}.py")

if not (args.test or args.submit):

    if path.exists():
        print(f"🎅 File '{path}' already exists!")
    else:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(Path("template.py").read_text().format(year=args.year, day=args.day))
        print(f"Created file '{path}'")

    if input("Open website? Y/n").upper() in ("Y", ""):
        webbrowser.open(f"https://adventofcode.com/{args.year}/day/{args.day}")
else:

    if not path.exists():
        print(f"Solution '{path}' does not exist. Is the date correct?")
    elif (args.test):
        run_tests(args.year, args.day, args.part)
    elif (args.submit):
        if args.part is None:
            print("Please provide a part")
        else:
            result = run_tests(args.year, args.day, args.part)[0]

            if result is None:
                print("No results found, canceling submit")
                exit(0)
            
            submit(args.year, args.day, args.part, result)