from aoc.helpers import aoc

# https://adventofcode.com/2022/day/2

@aoc(2022, 2)
def main(input):
    rounds = [
        x.split() for x in input.strip().split('\n')
    ]
    score = 0
    for round in rounds:

        your = round[1]
        other = round[0]

        choices = {
            "X": 1, # rock
            "Y": 2, # paper
            "Z": 3, # scissor
            "A": 1, # rock
            "B": 2, # paper
            "C": 3 # scissor
        }

        score += choices[your]

        if choices[your] == choices[other]:
            score += 3
        elif any((
            (your == "Y" and other == "A"),
            (your == "X" and other == "C"),
            (your == "Z" and other == " B")
            )):
            score += 6
    
    print(score)
