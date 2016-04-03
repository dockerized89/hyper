__author__ = 'elopptj'


def first_name(name):
    return name.split()[0]


def main():
    scientists = ['Marie Curie', 'Albert Einstein', 'Niels Bohr', 'Issac Newton', 'Dmitri Mendeleev', 'Antoine Lavosier', 'Carl Linnaues', 'Alfred Wegener',
                  'Charles Darwin']

    sorted_first = sorted(scientists, key=first_name)

    print(sorted_first)

    sorted_last = sorted(scientists, key=lambda name: name.split()[-1])

    print(sorted_last)


if __name__ == '__main__':
    main()
