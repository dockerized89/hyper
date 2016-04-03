import os
import sys
sys.path.append(os.getcwd())


class Bucket(object):
    """
        Class representing a bucket object
    """
    def __init__(self, author, message):
        # The bucket wants an author and a message
        self.author = author
        self.message = message

    def get_bucket(self):
        # Returns a python dictionary, containing
        # author and message
        return {'author':self.author.get_name(),
                'message':self.message}

    def get_bucket_author(self):
        # Returns a python dictionary, containing
        # author and message
        return {'author': self.author.get_name(),
                'message': self.message}


class Author(object):
    # Init function executed when object is created
    def __init__(self, name):
        self.__name = name

    # Returns the name of the user
    def get_name(self):
        return self.__name

