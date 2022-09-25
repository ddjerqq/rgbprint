"""
RGBPRINT 4.0.0
--------------

This module has tools for printing colors on your terminal, printing gradients, and more.


Modules:
--------

- rgbprint

- Color

- gradient_print

- gradient_scroll

- gradient_change


Examples
---------
rgbprint
    >>> from rgbprint import rgbprint
    >>> rgbprint("hello", color="red")

Color creation
    >>> from rgbprint import Color
    >>> red0 = Color.red
    >>> red1 = Color(0xFF0000)
    >>> red2 = Color("FF0000")
    >>> red3 = Color("#FF0000")
    >>> red4 = Color(255, 0, 0)
    >>> red5 = Color((255, 0, 0))

gradient_print
    >>> from rgbprint import gradient_print
    >>> gradient_print("hello", start_color="red", end_color="yellow")

gradient_scroll
    >>> from rgbprint import gradient_scroll
    >>> gradient_scroll("hello", start_color="red", end_color="yellow", delay=0.3, times=5, reverse=False)

gradient_change
    >>> from rgbprint import gradient_change
    >>> gradient_change("hello", start_color="red", end_color="yellow", delay=0.3, times=5, reverse=False)


Notes:
------

- the prefererd way of accessing named colors is: `Color.<name>`

"""

from __future__ import annotations

import os
from typing import Tuple, List, Union

from .rgbprint import rgbprint
from .color import Color
from .gradient import (
    gradient_print,
    gradient_scroll,
    gradient_change,
)

ColorType: Union[int, str, Union[Tuple[int, int, int], List[int, int, int]], Color]

__all__ = (
    "Color",
    "rgbprint",
    "gradient_print",
    "gradient_change",
    "gradient_scroll",
)

__version__ = "4.0.2"

# initialize colors, this works for *most* terminals.
os.system("")
