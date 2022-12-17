def dup(li: str):
    li = sorted(li)
    for i in range(len(li)-1):
        if li[i] == li[i+1]:
            return True
    return False


def scan(file, pattern=4):
    numbers = []
    with open(file) as f:
        text = f.readlines()
        count = 1
        for i in range(len(text[0]) - pattern):
            if dup(text[0][i:i+pattern]):
                count += 1
            else:
                print(f'{len(text[0][:count+pattern-1])}')
                numbers.append(count + pattern-1)
                count = 0
                break
    print(numbers)


if __name__ == '__main__':
    scan('input.txt')
