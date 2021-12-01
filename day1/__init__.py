from collections import deque


def solve_part_one(content):
    return sum(
        map(lambda measurement: 0 if measurement[0] == 0 else
        1 if content[measurement[0]] > content[measurement[0] - 1] else 0,
            enumerate(content))
    )


def solve_part_two(content):
    ret = map(sum, window(content))
    return solve_part_one(list(ret))


def window(seq, n=3):
    it = iter(seq)
    win = deque((next(it, None) for _ in range(n)), maxlen=n)
    yield win
    append = win.append
    for e in it:
        append(e)
        yield win
