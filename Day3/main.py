import string

matches = []


def find_p(s: str):
    one = s[:int(len(s) / 2)].strip()
    two = s[int(len(s) / 2):].strip()
    for i in one:
        for j in two:
            if i == j:
                return i
        pass


def score(c: str):
    if c in string.ascii_lowercase:
        return ord(c) - 96
    else:
        return ord(c) - 38


def run(file):
    with open(file) as f:
        ruck = f.readlines()
        for line in ruck:
            matches.append(score(find_p(line)))
    print(sum(matches))


if __name__ == '__main__':
    run("input.txt")
