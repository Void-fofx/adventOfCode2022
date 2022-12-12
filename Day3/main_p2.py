import string

groups = []
scores = []


def find_badge(li: []):
    for c in li[0]:
        if c in li[1] and c in li[2]:
            return c
        else:
            pass


def score(c: str):
    if c in string.ascii_lowercase:
        return ord(c) - 96
    else:
        return ord(c) - 38


def run(file):
    with open(file) as f:
        ruck = f.readlines()
        while len(ruck) > 0:
            temp = []
            for i in range(0, 3):
                temp.append(ruck.pop().strip())
            groups.append(temp)
    for g in groups:
        scores.append(score(find_badge(g)))
    print(sum(scores))


if __name__ == '__main__':
    run("input.txt")
