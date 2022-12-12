def to_ints(arr: []):
    temp = arr[0].split("-")
    temp2 = arr[1].split("-")
    ran = range(int(temp[0]), int(temp[1]) + 1)
    ran2 = range(int(temp2[0]), int(temp2[1]) + 1)
    if ran[0] in ran2 or ran[-1] in ran2:
        return True
    elif ran2[0] in ran or ran2[-1] in ran:
        return True
    else:
        return False


def run(file):
    total = 0
    with open(file) as f:
        sections = f.readlines()
        for line in sections:
            line = line.strip()
            line = line.split(",")
            if to_ints(line):
                total += 1
        print(total)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run('input.txt')
