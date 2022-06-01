from typing import Tuple, Union
from .parser import ColorParser


__all__ = ["Color"]


class Color:
    """
    A class to represent a color.
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    color class.
    can be printed, and will work with the RGB print function.  \n
    """
    def __init__(self, color: Union[str, int, Tuple[int, int, int]]):
        """
        Initialize a color.
        :param color: this can be a string "RRGGBB" or "#RRGGBB",
        a color name (see supported colors), integer color (0xFF00FF) or a (r, g, b) tuple of integers (0-255).

        raises:
            ValueError: if the color is not supported.
        """
        rgb = ColorParser.parse(color)
        self.r, self.g, self.b = rgb

    def __str__(self):
        return "\033[38;2;{0};{1};{2}m".format(self.r, self.g, self.b)

    def __eq__(self, other):
        return self.r == other.r and self.g == other.g and self.b == other.b

    def __repr__(self):
        return "Color({0}, {1}, {2})".format(self.r, self.g, self.b)

    # feature in the future
    #
    # def __add__(self, other):
    #     return Color((self.r + other.r, self.g + other.g, self.b + other.b))
    #
    # def __sub__(self, other):
    #     return Color((self.r - other.r, self.g - other.g, self.b - other.b))
    #
    # def __mul__(self, other):
    #     return Color((self.r * other, self.g * other, self.b * other))
    #
    # def __floordiv__(self, other):
    #     return Color((self.r // other, self.g // other, self.b // other))
