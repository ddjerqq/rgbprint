from typing import Tuple, Union

from .parser import ColorParser
from .supported_colors import SUPPORTED_COLORS_LITERAL


__all__ = ["Color"]


class Color:
    """
    A class to represent a color.
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    this class automatically clips wrong color values to 0-255. \n
    can be printed, and will work with the RGB print function.  \n
    """
    def __init__(self, color: Union[str, SUPPORTED_COLORS_LITERAL, Tuple[int, int, int]]):
        """
        Initialize a color.
        :param color: this can be a string RRGGBB or #RRGGBB, a color name, or a tuple of RGB values.
        """
        res = ColorParser.parse(color)
        if res is not None:
            r, g, b = ColorParser.parse(color)
        else:
            raise RuntimeWarning(f"{color} is not a valid color")
        self.r = r
        self.g = g
        self.b = b

    def __str__(self):
        return f"\033[38;2;{self.r};{self.g};{self.b}m"

    def __repr__(self):
        return f"Color({self.r}, {self.g}, {self.b})"

    def __eq__(self, other):
        return self.r == other.r and self.g == other.g and self.b == other.b

    def __add__(self, other) -> "Color":
        return Color((self.r + other.r, self.g + other.g, self.b + other.b))

    def __sub__(self, other) -> "Color":
        return Color((self.r - other.r, self.g - other.g, self.b - other.b))

    def __mul__(self, other) -> "Color":
        return Color((self.r * other, self.g * other, self.b * other))

    def __floordiv__(self, other) -> "Color":
        return Color((self.r // other, self.g // other, self.b // other))
