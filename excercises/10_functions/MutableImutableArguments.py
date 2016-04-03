__author__ = 'elopptj'


def some_func(number):
    number += 1


def some_other_func(aList):
    aList[0] = "changed"


def main():
    number = 3

    some_func(number)
    print(number)

    aList = ["one", "two", "three"]
    some_other_func(aList)
    print(aList)


if __name__ == '__main__':
    main()
