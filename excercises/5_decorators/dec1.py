__author__ = 'elopptj'


def div_decorate(f):
    def wrapper(name):
        return '<div>%s</div>' % f(name)

    return wrapper


def strong_decorate(f):
    def wrapper(name):
        return '<strong>%s</strong>' % f(name)

    return wrapper


def h1_decorate(f):
    def wrapper(name):
        return '<h1>%s</h1>' % f(name)

    return wrapper

def p_decorate(f):
    def wrapper(name):
        return '<p>%s</p>' % f(name)

    return wrapper

@p_decorate
@h1_decorate
@strong_decorate
@div_decorate
def gen_text(name):
    return 'Hi my name is ' + name


def main():
    s1 = gen_text('Erik')
    s2 = gen_text('Kelvin')

    print(s1)
    print(s2)


if __name__ == '__main__':
    main()
