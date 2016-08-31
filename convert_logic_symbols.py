#!/usr/bin/python2.7

'''
Written for converting strings of predicate logic from one symbol set, to another.

Could be used as a general purpose substring replacer
'''

import sys

symbol_set_map = {
    '^':'&',
    '$':'<>',
    '!':'>',
    '_':'V',
    ':':'~',
}

assert len(sys.argv) == 2, 'Must be called with one argument: string to convert.'

print(''.join(map(lambda char: symbol_set_map[char] if char in symbol_set_map.keys() else char, sys.argv[1])))
