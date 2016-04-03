__author__ = 'elopptj'


class CallCount():
    def __init__(self, f):
        self.f = f
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.f(*args, **kwargs)


@CallCount
def hello(name):
    print('Hello ' + name)


def main():
    hello('Erik')
    hello('Filip')
    hello('Kelvin')
    print(hello.count)


if __name__ == '__main__':
    main()
