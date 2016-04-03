__author__ = 'elopptj'


def main():
    numbersAsStrings = ['1', '15', '344', '19', '22']

    convertedToString = []

    #Task 1
    for x in numbersAsStrings:
        convertedToString.append(int(x))

    print(convertedToString)


    #Task 2

    convertedToString = [int(x) for x in numbersAsStrings]

    print(convertedToString)

    #Task 3

    convertedToString = [int(x) for x in numbersAsStrings if len(x) <= 2]

    print(convertedToString)

if __name__ == '__main__':
    main()
