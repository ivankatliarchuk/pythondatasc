def split_and_join(line):
    splitted = line.split(' ')
    print(splitted)
    return "-".join(splitted)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)