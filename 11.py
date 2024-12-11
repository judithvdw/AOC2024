from collections import defaultdict

from utils.parsing import parse_ints


def blink(stones):
    new_stones = defaultdict(int)
    for stone, n in stones.items():
        if stone == 0:
            new_stones[1] += n
        elif len(str_stone := str(stone)) % 2 == 0:
            left, right = str_stone[:len(str_stone) // 2], str_stone[len(str_stone) // 2:]
            new_stones[int(left)] += n
            new_stones[int(right)] += n
        else:
            new_stones[stone * 2024] += n
    return new_stones


def blinker(stones, n):
    for _ in range(n):
        stones = blink(stones)
    return stones


with open("inputs/11.txt") as f:
    starting_stones = parse_ints(f.readlines())[0]

stones = defaultdict(int)
for s in starting_stones:
    stones[s] += 1

print(f"Part 1: {sum(blinker(stones, 25).values())}")
print(f"Part 2: {sum(blinker(stones, 75).values())}")
