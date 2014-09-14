#!/usr/bin/env python
from distutils.core import setup

readme = open('README.rst').read()

setup(
    name='random-string',
    version='1.00',
    author_email='gattster@gmail.com',
    author='Philip Gatt',
    description="A function that generates random strings",
    long_description=readme,
    url='http://github.com/defcube/random_string/',
    py_modules=["random_string"],
    data_files=[('', ['README.rst'])],
    )