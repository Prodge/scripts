'''
Add line spacing on a single line exception
'''

import sys

exception = sys.argv[1]

print '\n\n\n'
print exception.replace('File', '\n')

