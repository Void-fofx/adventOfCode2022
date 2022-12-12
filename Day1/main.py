def to_list(file):
    arr = []
    with open(file) as f:
        lines = [line.rstrip() for line in f]
        count = 0
        for i in lines:
            if i != '':
                count += int(i)
            else:
                arr.append(count)
                count = 0
    return sorted(arr)
### part 1 ###
#       num = 0
#        for large in arr:
#            if large > num:
#               num = large
#        print(f"Most Calories: {num}")


if __name__ == '__main__':
    sort = to_list("input.txt")
    print(sum(sort[-3:]))

