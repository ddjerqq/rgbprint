import os

from .src.fore import *
from .src.gradient import *
from .src.rgbprint import rgbprint
from .src.demo import *


__all__ = [
    "demo",
    "Fore",
    "rgbprint",
    "gradient_print",
    "gradient_change",
    "gradient_scroll",
    "gradient_scroll_async"
]

__version__ = "3.0.0"


# magic initialization of colors :0
os.system("")

