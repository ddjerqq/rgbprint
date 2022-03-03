"""
made by ddjerqq.
~~~~~~~~~~~~~~~~
This is supposed to be a replacement for print, with support for
kwarg color \n
>>> from rgbprint.new_print import _print as print
>>> from rgbprint.colors import Colors
>>> print("Hello world", Colors.RED)
>>> print("lorem ipsum", "dolor sit amet", end="\n\n", sep="$", color=0x00ff00)
>>> print("lorem ipsum", color=Colors.random())
>>> print("lorem ipsum", color=Colors.random(range(127), range(127, 255), range(127, 255)))
"""

import os
os.system("")
