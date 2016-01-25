#!/usr/bin/env python

from setuptools import setup

setup(
    # GETTING-STARTED: set your app name:
    name='Learn Tibetan',
    # GETTING-STARTED: set your app version:
    version='1.0',
    # GETTING-STARTED: set your app description:
    description='Learn Tibetan App',
    # GETTING-STARTED: set author name (your name):
    author='Tsering Döndrup',
    # GETTING-STARTED: set author email (your email):
    author_email='budismoclasico@gmail.com',
    # GETTING-STARTED: set author url (your url):
    url='http://www.budismoclasico.org/',
    # GETTING-STARTED: define required django version:
    install_requires=[
        'Django==1.8.4'
    ],
    dependency_links=[
        'https://pypi.python.org/simple/django/'
    ],
)
