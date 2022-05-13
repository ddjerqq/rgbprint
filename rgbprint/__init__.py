"""
rgbprint \n
-----------
print colors and gradients in your terminal!
-------------------------------------------- \n
usage: \n
>>> from rgbprint import * \n
>>> rgbprint("some", "text", color="red") \n
>>> gradient_print("some", "text", start_color="red", end_color="blue") \n
>>> for _ in load_bar("red", "blue", 10): \n
>>>     ... \n
"""


import os

from .fore import *
from .gradient import *
from .load_bar import *
from .demo import *


__all__ = [
    "demo",
    "Fore",
    "rgbprint",
    "gradient_print",
    "gradient_change",
    "gradient_scroll",
    "gradient_scroll_async",
]

__version__ = "3.0.0"

os.system("")
# initialize colors lol
