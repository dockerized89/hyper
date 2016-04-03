__author__ = 'elopptj'


class Point:
    count = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        Point.count += 1

    def __del__(self):
        Point.count -= 1

    def __str__(self):
        return "x = " + str(self.x) + " y = " + str(self.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


def main():
    p1 = Point(10, 34)
    p2 = Point(4, 67)

    print(p1)

    p3 = p1 + p2

    print(Point.count)
    del p1
    del p2

    print(p3.count)


if __name__ == '__main__':
    main()
