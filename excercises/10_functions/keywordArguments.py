__author__ = 'elopptj'


def func(number, name, age=20):
    print('number =', number, 'name=', name, 'age=', age)


def main():
    func(13, 'John')
    func(name='Sara', number=22)
    func(11, age=44, name='Bob')


if __name__ == '__main__':
    main()
