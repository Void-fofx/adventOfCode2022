di = {
    "A": "rock",  # Rock
    "B": "paper",  # Paper
    "C": "scissors",  # Scissors
    "X": "rock",  # Rock
    "Y": "paper",  # Paper
    "Z": "scissors"  # Scissors
}


def compare(li: []):
    if di[li[1]] == "rock":
        if di[li[0]] == "rock":
            return 1 + 3
        elif di[li[0]] == "paper":
            return 1 + 0
        else:
            return 1 + 6
    if di[li[1]] == "paper":
        if di[li[0]] == "rock":
            return 2 + 6
        elif di[li[0]] == "paper":
            return 2 + 3
        else:
            return 2 + 0
    if di[li[1]] == "scissors":
        if di[li[0]] == "rock":
            return 3 + 0
        elif di[li[0]] == "paper":
            return 3 + 6
        else:
            return 3 + 3


def run(file):
    total = 0
    with open(file, "r") as f:
        for i in f:
            n = i.strip()
            total += int(compare(n.rsplit(" ")))
    print(f"score = {total}")


if __name__ == "__main__":
    run("input.txt")
