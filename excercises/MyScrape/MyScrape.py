#!/usr/bin/python3

import MyHttp
import MyParser
import sys

# try to assign the subdomain and path values
# if the assignment fails, just use default values
try:
    subdomain, path = sys.argv[1:]
except:
    subdomain, path = 'milwaukee', '/eng/'

# instantiate the parser
parser = MyParser.ClParser()

# instantiate the page
page = MyHttp.Page(subdomain + '.craigslist.org', path)

# get the page and feed it to the parser
parser.feed(page.get_as_string())

# display the results
print('################\n    Results:\n################\n', parser.results)
