import os
import sys
sys.path.append(os.getcwd())

"""
    Database configuration.
"""
import os
# Resolve path to sqlite db file
basedir = os.path.abspath(os.path.dirname(__file__))

# Resolve DB file name
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

# Optional migration data path (Maybe we'll get to this.)
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')