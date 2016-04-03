__author__ = 'elopptj'


class Base(object):
    def __init__(self):
        print("We are in base constructor")


class A(Base):
    def __init__(self):
        print("We are in A constructor")
        Base.__init__(self)


class B(Base):
    def __init__(self):
        print("We are in B constructor")
        Base.__init__(self)


class C(A, B):
    def __init__(self):
        print("We are in C constructor")
        A.__init__(self)
        B.__init__(self)


def main():
    c = C()


if __name__ == '__main__':
    main()
