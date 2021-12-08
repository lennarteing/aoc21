with open('../resources/day8input') as f:
    data = [line.strip() for line in f.readlines()]

data = [(line.split(' | ')[0], line.split(' | ')[1]) for line in data]
data = [(inp.split(), out.split()) for inp, out in data]

# part 1
l = {
    1: 2,
    4: 4,
    7: 3,
    8: 7,
}

from collections import Counter

count_output = Counter([len(s) for inp, out in data for s in out])
part1 = sum(count_output[n] for n in (l[1], l[4], l[7], l[8]))

candidates = {
    5: [2, 3, 5],
    6: [0, 6, 9]
}

# part 2
def deduce(inp):
    d = {s: len(s) for s in inp}

    others = {5: [], 6: []}

    for k, v in d.items():
        letters = {_ for _ in k}
        if v == l[1]:
            one = letters
        elif v == l[7]:
            seven = letters
        elif v == l[4]:
            four = letters
        elif v == l[8]:
            eight = letters
        else:
            others[v].append(letters)

    top = seven - one

    nine = [letters for letters in others[6] if len(letters - (seven | four)) == 1][0]
    bottom = nine - (seven | four)

    three = [letters for letters in others[5] if len(letters - (seven | bottom)) == 1][0]
    topleft = nine - three
    bottomleft = eight - nine

    zero = (seven | bottom | bottomleft | topleft)

    six = [letters for letters in others[6] if letters not in [zero, one, three, four, seven, eight, nine]][0]

    topright = eight - six
    bottomright = one - topright

    two = (three | bottomleft) - bottomright
    five = (six - bottomleft)

    return dict(enumerate([zero, one, two, three, four, five, six, seven, eight, nine]))

part2 = 0
for inp, out in data:
    lineres = ''
    nums = deduce(inp)
    for s in out:
        lineres += str([k for k, v in nums.items() if v == set(c for c in s)][0])

    part2 += int(lineres)

print(f'part 1: {part1}')
print(f'part 2: {part2}')
