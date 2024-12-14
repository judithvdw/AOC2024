from utils.parsing import parse_ints


def use_machine(machine, add):
    ax, ay, bx, by, px, py = machine
    px += add
    py += add
    B, rb = divmod((ax * py - px * ay), (ax * by - bx * ay))
    A, ra = divmod((px - B * bx), ax)
    if ra == 0 and rb == 0:
        return A * 3 + B
    else:
        return 0


with open("inputs/13.txt") as f:
    raw = parse_ints(f.readlines())

machines = [tuple([item for sublist in raw[i:i + 3] for item in sublist]) for i in range(0, len(raw), 4)]

print(sum(use_machine(machine, 0) for machine in machines))
print(sum(use_machine(machine, 10_000_000_000_000) for machine in machines))

