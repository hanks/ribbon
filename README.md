ribbon[![Coverage Status](https://coveralls.io/repos/hanks/ribbon/badge.png?branch=master)](https://coveralls.io/r/hanks/ribbon?branch=master)[![Build Status](https://travis-ci.org/hanks/ribbon.svg?branch=master)](https://travis-ci.org/hanks/ribbon)[![PyPI version](https://badge.fury.io/py/ribbon.svg)](http://badge.fury.io/py/ribbon)[![PyPi downloads](https://pypip.in/d/ribbon/badge.png)](https://crate.io/packages/ribbon/)![pep8](http://img.shields.io/badge/pep8-passing-brightgreen.svg)[![Supported Python versions](https://pypip.in/py_versions/ribbon/badge.svg)](https://pypi.python.org/pypi/ribbon/)[![status](https://sourcegraph.com/api/repos/github.com/hanks/ribbon/.badges/status.png)](https://sourcegraph.com/github.com/hanks/ribbon)
===========================

A simple color print library for console.

## Version History

###_VERSION_ 1.0 - 2014/07/30
+ First release upon the world  

## Why
Just inspired by **fabric.colors** module, and want to try how to release a python package to PyPi, so create this simple library.  

The ribbon library can help you to print colorful text in console more easily, and even you can print **rainbow-like** text. Just for fun!!

## Demo
![demo](https://raw2.github.com/hanks/ribbon/master/demo/demo.png)

##Usage
```
from ribbon import red
print(red('This text is red'))

from ribbon import red, green
print(red('This is red and ' + green('that is green')))

from ribbon import rainbow
print(rainbow('This is a rainbow-like text!'))
```

## Install
```
pip install ribbon
```

## Contribution
**Waiting for your pull request**

## Lisence
MIT Lisence