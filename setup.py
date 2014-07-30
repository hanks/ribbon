#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from distutils.core import setup

here = os.path.abspath(os.path.dirname(__file__))

def read(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    return content
    
long_description = read('{}/{}'.format(here, 'README.md'))

setup(
    name="ribbon",
    version='1.0.0',
    author='hanks',
    author_email='zhouhan315@gmail.com',
    url='https://github.com/hanks/ribbon',
    description="A simple color console print library.",
    long_description=long_description,
    keywords='color console print',
    license='MIT',
    py_modules=['ribbon'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Environment :: Console",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
    ],
)
