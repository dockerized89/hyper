__author__ = 'elopptj'


def func():
    return 1, 2, 3, 4


def main():
    print(func())
    a, b, c, d = func()
    print(a, b, c, d)


if __name__ == '__main__':
    main()
