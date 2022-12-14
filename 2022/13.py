from aoc.helpers import aoc

from pprint import pprint

# https://adventofcode.com/2022/day/13

def run_packet(packet):

    match packet:
            case [[*L], [*R]]:
                for i, item in enumerate(zip(L, R)):
                    res = run_packet(item)
                    if res is not None:
                        return res
                if len(L) > len(R):
                    return False
                elif len(L) == len(R):
                    return None
            case [[*L], R]:
                return run_packet((L, [R]))
            case [L, [*R]]:
                return run_packet(([L], R))
            case [L, R]:
                if L > R:
                    return False
                elif L == R:
                    return None
    return True


@aoc(2022, 13)
def part1(input):

    packets = tuple(tuple(eval(s) for s in p.splitlines()) for p in input.split("\n\n"))
    
    sum = 0
    for i, packet in enumerate(packets):
        if run_packet(packet):
            sum += i + 1

    return sum



@aoc(2022, 13)
def part2(input):

    input += "\n[[2]]\n[[6]]"
    
    packets = [eval(p) for p in "\n".join(input.split("\n\n")).splitlines()]
    
    for _, packet in list(enumerate(packets)):
        packets.remove(packet)
        
        for x, other_packet in list(enumerate(packets)):
            if run_packet((packet, other_packet)):
                packets.insert(x, packet)
                break
        else:
            packets.append(packet)

    return (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)

