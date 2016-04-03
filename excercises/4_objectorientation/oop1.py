__author__ = 'elopptj'


class MyClass(object):
    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

    def __str__(self):
        return str(self.value)


def main():
    myclass = MyClass("test")
    var = myclass.getValue()
    print(var)
    print(myclass)


if __name__ == '__main__':
    main()
