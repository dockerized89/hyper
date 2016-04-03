__author__ = 'elopptj'


class Trace():
    def __init__(self):
        self.enabled = True

    def __call__(self, f):
        def wrapper(*args, **kwargs):
            if self.enabled:
                print('Calling {}'.format(f))
            return f(*args,**kwargs)
        return wrapper

tracer = Trace()

@tracer
def rotate_list(l):
    return l[1:] + [l[0]]

@tracer
def main():
    myList = [1,2,3]
    l = rotate_list(myList)

    print(l)

if __name__ == '__main__':
    main()
