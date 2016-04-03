__author__ = 'elopptj'


class Base():
    def __init__(self):
        print("We are in base constructor")

    def __del__(self):
        print("We are in base destructor")


class A(Base):
    def __init__(self):
        print("We are in A constructor")
        super().__init__()

    def __del__(self):
        print("We are in A destructor")
        super().__del__()


class B(Base):
    def __init__(self):
        print("We are in B constructor")
        super().__init__()

    def __del__(self):
        print("We are in B destructor")
        super().__del__()


class C(A, B):
    def __init__(self):
        print("We are in C constructor")
        super().__init__()

    def __del__(self):
        print("We are in C destructor")
        super().__del__()


def main():
    c = C()
    print(C.mro())

    del c


if __name__ == '__main__':
    main()
