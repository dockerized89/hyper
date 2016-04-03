__author__ = 'elopptj'


def raiseTo(exp):
    def raiseToExp(x):
        return pow(x, exp)

    return raiseToExp


def main():
    square = raiseTo(2)
    cube = raiseTo(3)

    print(square(10))
    print(cube(10))


if __name__ == '__main__':
    main()
