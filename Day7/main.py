def run(file):
    with open(file) as f:
        text = f.readlines()
        print(text)


if __name__ == '__main__':
    run('input.txt')
