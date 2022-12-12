def to_ints(arr: []):
    temp = arr[0].split("-")
    temp2 = arr[1].split("-")
    if int(temp[0]) == int(temp[1]):
        print()
        if int(temp2[0]) <= int(temp[0]) <= int(temp2[1]):
            return True
        else:
            return False
    if int(temp2[0]) == int(temp2[1]):
        if int(temp[0]) <= int(temp2[0]) <= int(temp[1]):
            return True
        else:
            return False
    if int(temp[0]) <= int(temp2[0]) and int(temp[1]) >= int(temp2[1]):
        return True
    elif int(temp[0]) >= int(temp2[0]) and int(temp[1]) <= int(temp2[1]):
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
