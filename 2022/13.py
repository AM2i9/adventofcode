from aoc.helpers import aoc

# https://adventofcode.com/2022/day/13

def run_packet(packet):

    if (isinstance(packet[0], list) and isinstance(packet[1], list)) and len(packet[0]) < len(packet[1]):
        return False
    
    match packet:
            case [[*_], [*_]]:
                for item in zip(*packet):
                    if not run_packet(item):
                        return False
            case [[*L], R]:
                return run_packet((L, [R]))
            case [L, [*R]]:
                return run_packet(([L], R))
            case [L, R]:
                if L > R:
                    return False
    return True


@aoc(2022, 13)
def part1(input):
    input="""[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""

    packets = tuple(tuple(eval(s) for s in p.splitlines()) for p in input.split("\n\n"))
    
    sum = 0
    for i, packet in enumerate(packets):
        print(run_packet(packet))

    return sum



@aoc(2022, 13)
def part2(input):
    ...
