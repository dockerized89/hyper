from collections import namedtuple

__author__ = 'elopptj'


def main():
    book = namedtuple("book", "author title genre")

    books = [
        book("Kalle", "Anka", "adventure"),
        book("Erik", "Thief of times", "scifi"),
        book("Olle", "The dispossed", "scifi"),
        book("Kelvin", "A Wizard if Earthsea", "fantasy"),
        book("Le Guin", "The thief", "fantasy"),
        book("Filip", "Anka1", "fantasy"),
        book("Filip", "Anka2", "fantasy")
    ]

    fantasy_authors = {x.author for x in books if x.genre == 'fantasy'}



    fantasy_titles = {b.title: b for b in books if b.genre == 'fantasy'}

    for key, book in fantasy_titles.items():
        print(key, ' : ', book.author)


if __name__ == '__main__':
    main()
