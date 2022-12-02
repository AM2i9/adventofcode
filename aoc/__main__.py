import argparse
from pathlib import Path

parser = argparse.ArgumentParser(
    prog = "AoC Helper",
    description = "Helper program for Advent of Code",
)

parser.add_argument("year", type=int)
parser.add_argument("day", type=int)

args = parser.parse_args()

path = Path(f"{args.day:>02}.py")

if path.exists():
    print(f"File '{path}' already exists!")
else:
    path.write_text(Path("template.py").read_text().format(year=args.year, day=args.day))
    print(f"Created file '{path}'")