from aoc.helpers import aoc

# https://adventofcode.com/2022/day/2

@aoc(2022, 2)
def part2(input):
    rounds = [
        x.split() for x in input.strip().split('\n')
    ]
    choices = {
        "A": 1, # rock
        "B": 2, # paper
        "C": 3 # scissor
    }
    score = 0
    for round in rounds:
        match round:
            case [other, "Y"]:
                score += choices[other] + 3
            case [other, "Z"]:
                your = choices[other] + 1
                if your > 3:
                    your = 1
                score += your + 6
            case [other, "X"]:
                your = choices[other] - 1
                if your < 1:
                    your = 3
                score += your

    return score


@aoc(2022, 2)
def part1(input):
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
            (your == "Z" and other == "B")
            )):
            score += 6
    
    return score
