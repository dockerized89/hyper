__author__ = 'elopptj'


class URLParser(object):
    def __init__(self, url):
        self.url = url
        if '://' not in self.url:
            # http -> protocol
            # www.google.se -> host
            # /search_for_something/ -> page
            self.protocol = ''
            self.host = url.split('/')[0]
            self.page = '/'.join(self.url.split('/')[1:])
        else:
            self.protocol = self.url.split('://')[0]
            self.host = self.url.split('/')[2]
            self.page = '/'.join(self.url.split('/')[3:])

    def getProtocol(self):
        return self.host


    def getHost(self):
        return self.host

    def getPage(self):
        return self.page

    def __repr__(self):
        info = []
        info.append('Host: {0}'.format(self.host))
        info.append('Page: {0}'.format(self.page))
        info.append('Protocol {0}'.format(self.protocol))

        joined_string = '\n'.join(info)

        return joined_string


def main():
    parser = URLParser('http://www.google.se/search/me')
    print('Host: ', parser.getHost())
    print('Page: {0}'.format(parser.getPage()))
    print('Protocol:', parser.getProtocol())

    #print(parser)

if __name__ == '__main__':
    main()
