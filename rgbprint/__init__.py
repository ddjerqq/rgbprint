"""
# TODO add docs here
"""


import os

from .fore     import *
from .rgbprint import *
from .gradient import *
from .parser   import ColorParser
from .color    import *
from .load_bar import *

__all__ = [
    "Fore",
    "Color",
    "ColorParser",
    "rgbprint",
    "gradient_print",
    "gradient_change",
    "gradient_scroll",
    "load_bar",
]

__version__ = "3.0.4"

os.system("")
# initialize colors lol
