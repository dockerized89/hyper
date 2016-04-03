__author__ = 'elopptj'

import unittest

from urlparser import URLParser


def fetchURL(url):
    class URL():
        def __init__(self, url):
            self.url = url

    return URL(url)


class MyTestCase(unittest.TestCase):
    def testHTTPProtocl(self):
        url = fetchURL("http://www.some.com/index.html")
        parser = URLParser(url.url)
        protocol = parser.getProtocol()

        self.assertEqual(protocol, "http")

    def testFTPProtocol(self):
        url = fetchURL("ftp://www.some.com/index.html")
        parser = URLParser(url.url)
        protocol = parser.getProtocol()

        self.assertEqual(protocol, "ftp")

    def testNoProtocol(self):
        url = fetchURL("www.some.com/index.html")
        parser = URLParser(url.url)
        protocol = parser.getProtocol()

        self.assertEqual(protocol, "")

    def testUnknownProtocol(self):
        url = fetchURL("qwery://www.some.com/index.html")
        parser = URLParser(url.url)
        protocol = parser.getProtocol()

        self.assertEqual(protocol, "qwery")

    def testHost1(self):
        url = fetchURL("http://www.some.com/index.html")
        parser = URLParser(url.url)
        host = protocol = parser.getHost()

        self.assertEqual(host, "www.some.com")

    def testHost2(self):
        url = fetchURL("http://www.someothersite.com/index.html")
        parser = URLParser(url.url)
        host = protocol = parser.getHost()

        self.assertEqual(host, "www.someothersite.com")

    def testHostNoProtocol(self):
        url = fetchURL("www.someothersite.com/index.html")
        parser = URLParser(url.url)
        host = protocol = parser.getHost()

        self.assertEqual(host, "www.someothersite.com")


    def testHTTPPage(self):
        url = fetchURL("http://www.some.com/somefolder/index.html")
        parser = URLParser(url.url)
        protocol = parser.getPage()

        self.assertEqual(protocol, "somefolder/index.html")

    def testHTTPPage2(self):
        url = fetchURL("http://www.some.com/someootherfolder/index.html")
        parser = URLParser(url.url)
        protocol = parser.getPage()

        self.assertEqual(protocol, "someootherfolder/index.html")


    def testHTTPPageLong(self):
        url = fetchURL("http://www.some.com/someootherfolder/one/two/three/index.html")
        parser = URLParser(url.url)
        protocol = parser.getPage()

        self.assertEqual(protocol, "someootherfolder/one/two/three/index.html")

    def testHTTPPageWithoutProtocol(self):
        url = fetchURL("www.some.com/someootherfolder/one/two/three/index.html")
        parser = URLParser(url.url)
        protocol = parser.getPage()

        self.assertEqual(protocol, "someootherfolder/one/two/three/index.html")

    def testHTTPNoPageWithoutProtocol(self):
        url = fetchURL("www.some.com/")
        parser = URLParser(url.url)
        protocol = parser.getPage()

        self.assertEqual(protocol, "")

    def testHTTPNoPageWithProtocol(self):
        url = fetchURL("http://www.some.com/")
        parser = URLParser(url.url)
        protocol = parser.getPage()

        self.assertEqual(protocol, "")
if __name__ == '__main__':
    unittest.main()
