__author__ = 'elopptj'

from math import factorial


def factorial_count(number):
    pass


def main():
    list = range(100)
    [print(x) for x in list]

    pow_list = [x*x for x in list]

    print('-' * 10, ' NEW LIST ', '-'*10)
    [print(x) for x in pow_list]


if __name__ == '__main__':
    main()
