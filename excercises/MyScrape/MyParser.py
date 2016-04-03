'''
Parse html from craigslist
'''

from html.parser import HTMLParser


class ClParser(HTMLParser):
    # parser state
    # These variables store the current state of the parser as it reads the file
    date = ''  # The date for the current listing

    title = ''  # The title of the current listing

    link = ''  # The link to the current listing's details

    collectFor = None  # will use this to keep track of what kind of data we
    # are currently collecting for. valid options are:
    # 'date', 'title', and 'link'

    insideRow = False  # This flag keeps track of whether we are inside a "row"
    # "rows" have listing information

    # parser output
    results = ''  # the parser's output will be stored here

    def handle_starttag(self, tag, attrs):
        '''This function gets called when the parser encounters a start tag'''
        if tag == 'a' and self.insideRow:
            self.collectFor = 'title'

        for key, value in attrs:

            if (self.collectFor == 'title'
                and key == 'href'
                and not self.link):  # and not self.link makes sure it doesn't overwrite a preexisting value
                self.link = value

            if key == 'class':
                if value == 'row':
                    self.insideRow = True
                if value == 'ban':
                    self.collectFor = 'date'

    def handle_endtag(self, tag):
        '''This function is called when the parser encounters an end tag'''
        if tag == 'p':
            self.insideRow = False

            # is there data to output?
            if self.title + self.link:
                self.results += "\nDate: \t{0}\nTitle:\t{1}\nLink:\t{2}\n".format(
                    self.date,
                    self.title,
                    self.link)
            self.__reset_row()

    def handle_data(self, data):
        '''This function is called when the parser encounters data inside to tags'''
        if self.collectFor == 'date':
            self.date = data
        if self.collectFor == 'title' and not self.title:
            self.title = data

        self.collectFor = None  # when we're done collecting the data, reset this flag

    def __reset_row(self):
        '''This is a utility function to reset the parser's state after a row'''
        self.title = ''
        self.link = ''
        self.summary = ''
        self.collectFor = None
        self.insideRow = False
