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

import App

class User(App.db.Model):
    id = App.db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self):
        return '<User %r>' % (self.nickname)
