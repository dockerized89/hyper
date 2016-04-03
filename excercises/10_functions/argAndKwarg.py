__author__ = 'elopptj'


def func(f_arg, *argv):
    print('First argument is ', f_arg)
    for arg in argv:
        print('In argv we got', arg)


def func2(**kwarg):
    if kwarg is not None:
        for key, value in kwarg.items():
            print (key ,'=', value)


def main():
    func(1, 2, 3, 4, 5, 6, 7, "kalle")

    func2(a=5, b=6, c=44)


if __name__ == '__main__':
    main()
