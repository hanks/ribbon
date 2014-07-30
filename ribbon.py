#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Functions for wrapping string in ANSI color codes, mainly
using in console print.

Each function within this module except rainbow, returns
the input string text, wrapped with ANSI color codes for
the appropriate color.

Inspired by fabric.colors module, just for fun.

Usage:
    from ribbon import red

    print(red('This text is red'))
    print(red('This text is red', bold=True))

Also you can nest them:
    from ribbon import red, green

    print(red('This is red and ' + green('that is green')))

The difference from fabric.colors is rainbow function, it can
create rainbow-like text!
    from ribbon import rainbow

    print(rainbow('This is a rainbow-like text!'))
'''

__all__ = [
    'red',
    'green',
    'yellow',
    'blue',
    'magenta',
    'cyan',
    'white',
    'rainbow',
]

__author__ = 'hanks'


def _wrap_with(code):
    def inner(text, bold=False):
        '''Wrap text with color code

        Args:
            text, string, string that need to be transferred
            bold, boolean, text is needed to be bold or not

        Returns:
            string, wrapped text with color code
        '''
        c = code
        if bold:
            c = '1;{}'.format(c)
        return '\033[{}m{}\033[0m'.format(c, text)
    return inner

'''Basic color wrappers
'''
red = _wrap_with('31')
green = _wrap_with('32')
yellow = _wrap_with('33')
blue = _wrap_with('34')
magenta = _wrap_with('35')
cyan = _wrap_with('36')
white = _wrap_with('37')


def _doctest_basic_wrappers():
    '''
    >>> red('a')
    '\\x1b[31ma\\x1b[0m'
    >>> green('a', bold=True)
    '\\x1b[1;32ma\\x1b[0m'
    '''

# color func list for rainbow
rainbow_wrapper_list = [red, yellow, green, blue, magenta]


def _nsplit(text, step):
    '''Split text to small groups which contains n letter each

    >>> _nsplit('abc', 4)
    ['abc']
    >>> _nsplit('abc', 3)
    ['abc']
    >>> _nsplit('abc', 2)
    ['ab', 'c']
    >>> _nsplit('abc', 1)
    ['a', 'b', 'c']
    >>> _nsplit('', 1)
    []
    '''
    assert step > 0, 'step parameter in xrange() shoule '\
        'always be non-zero positive integer'
    return [text[i: i + step] for i in range(0, len(text), step)]


def _flatten(a_list):
    """Return a flatten list

    >>> _flatten([1, 2, 3])
    [1, 2, 3]
    >>> _flatten([1, (2, 'a'), 3])
    [1, (2, 'a'), 3]
    >>> _flatten([[(1, 2), (3, 4)], [('a', 'b'), ('c' ,'d')]])
    [(1, 2), (3, 4), ('a', 'b'), ('c', 'd')]
    >>> _flatten([])
    []
    """
    assert isinstance(a_list, list), 'a_list should be list type'
    res = []

    for element in a_list:
        if isinstance(element, list):
            res.extend(_flatten(element))
        else:
            res.append(element)

    return res


def rainbow(text, wrapper_list=rainbow_wrapper_list):
    '''Return fabulous rainbow-like texts used in console

    Args:
        text, target string
        wrapper_list, function list to wrap each letter in text

    Returns:
        wrapped string

    >>> rainbow('abc')
    '\\x1b[31ma\\x1b[0m\\x1b[33mb\\x1b[0m\\x1b[32mc\\x1b[0m'
    '''
    splitted_text_list = _nsplit(text, len(wrapper_list))
    zipped_tuple_list = _flatten([list(zip(wrapper_list, splitted_text))
                                  for splitted_text in splitted_text_list])
    wrapped_str = ''.join([wrapper(letter)
                           for wrapper, letter in zipped_tuple_list])

    return wrapped_str

if __name__ == '__main__':
    import doctest
    doctest.testmod()
