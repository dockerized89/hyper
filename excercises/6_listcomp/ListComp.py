__author__ = 'elopptj'


def main():
    words = 'One day I woke up and I believed as many as six impossible things before breakfast'.split()
    print(words)

    word_length = [len(word) for word in words]
    print(word_length)

    wordlen2 = []

    for word in words:
        wordlen2.append(len(word))

    print(wordlen2)

if __name__ == '__main__':
    main()
