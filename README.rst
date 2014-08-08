ribbon 
======

.. image:: https://coveralls.io/repos/hanks/ribbon/badge.png?branch=master
   :target: https://coveralls.io/r/hanks/ribbon?branch=master
   :alt: Coverage Status

.. image:: https://travis-ci.org/hanks/ribbon.svg?branch=master
   :target: https://travis-ci.org/hanks/ribbon
   :alt: Build Status

.. image:: https://badge.fury.io/py/ribbon.svg
   :target: http://badge.fury.io/py/ribbon
   :alt: PyPI version

.. image:: https://pypip.in/d/ribbon/badge.png
   :target: https://crate.io/packages/ribbon/
   :alt: PyPi downloads

.. image:: https://img.shields.io/badge/pep8-passing-brightgreen.svg
   :alt: pep8

.. image:: https://pypip.in/py_versions/ribbon/badge.svg
   :target: https://pypi.python.org/pypi/ribbon/
   :alt: Supported Python versions

.. image:: https://sourcegraph.com/api/repos/github.com/hanks/ribbon/.badges/status.png
   :target: https://sourcegraph.com/github.com/hanks/ribbon
   :alt: status

.. image:: https://sourcegraph.com/api/repos/github.com/hanks/ribbon/.counters/views.png
   :target: https://sourcegraph.com/github.com/hanks/ribbon
   :alt: views

simple color print library for console.

Version History
---------------

*VERSION 1.0 - 2014/07/30*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
+ First release upon the world  

Why
---
Just inspired by **fabric.colors** module, and want to try how to release a python package to PyPi, so create this simple library.  

The ribbon library can help you to print colorful text in console more easily, and even you can print **rainbow-like** text. Just for fun!!

Demo
----
.. image:: https://raw2.github.com/hanks/ribbon/master/demo/demo.png
   :alt: demo

Usage
-----
::

  from ribbon import red
  print(red('This text is red'))

  from ribbon import red, green
  print(red('This is red and ' + green('that is green')))

  from ribbon import rainbow
  print(rainbow('This is a rainbow-like text!'))

Install
-------
::

  pip install ribbon

Contribution
-------------
**Waiting for your pull request**

Lisence
-------
MIT Lisence
