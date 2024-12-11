def get_filesystem(diskmap):
    filesystem = []
    for i, num in enumerate(diskmap):
        if i % 2 == 0:
            filesystem.extend([i // 2] * int(num))
        else:
            filesystem.extend([None] * int(num))
    return filesystem


def defragment(filesystem):
    curr = 0
    while None in filesystem:
        last_item = filesystem.pop()
        if last_item is not None:
            next_none = filesystem.index(None, curr)
            filesystem[next_none] = last_item
            curr = next_none
    return filesystem


with open('inputs/09.txt') as f:
    diskmap = f.read().strip()

print(f'Part 1: {sum(i * num for i, num in enumerate(defragment(get_filesystem(diskmap))))}')
