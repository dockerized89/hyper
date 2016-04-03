__author__ = 'elopptj'


def main():
    file = open('data.txt', 'w')

    # writing
    try:
        file.write('This is the first line\n')
        file.write('This is the second line\n')
    finally:
        file.close()

    with open('data2.txt', 'w') as file2:
        file2.write('This is the first line\n')
        file2.write('This is the second line\n')

    # Reading

    file = open('data.txt', 'r')
    lines = file.readlines()  # Will read all lines into a list of strings

    for line in lines:
        print(line, end='')

    print()

    file = open('data.txt', 'r')
    first = file.read(1)
    second = file.read(8)
    print(first, second)
    file.close()

    print()

    # This is the old style of reading the text file. Don't use this as it is a waste of resources.

    file = open('data.txt', 'r')
    for line in file.readlines():
        print(line, end='')
    file.close()

    print()
    # Semi good solution but not the best.
    lines = list(open('data.txt', 'r'))
    for line in lines:
        print(line, end='')

    print()

    # Pro way to do it
    for line in open('data.txt'):
        print(line, end='')

    print()

    lines = [line.rstrip() for line in open('data.txt', 'r')]

    for line in lines:
        print(line)

    print()

    line = 'This is the sec'
    if line in open('data.txt'):
        print('The line is found')
    else:
        print('The line was not found')



if __name__ == '__main__':
    main()
