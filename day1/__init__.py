from collections import deque


def solve_part_one(content):
    return sum(map(lambda win: 1 if win[1] > win[0] else 0, window(content, n=2)))

def solve_part_two(content):
    ret = map(sum, window(content, n=3))
    return solve_part_one(list(ret))


def window(seq, n=3):
    it = iter(seq)
    win = deque((next(it, None) for _ in range(n)), maxlen=n)
    yield win
    append = win.append
    for e in it:
        append(e)
        yield win
