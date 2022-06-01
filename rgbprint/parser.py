import string
from typing import Tuple
from .supported_colors import SupportedColors


__all__ = ["ColorParser"]


class ColorParser:
    """
    the color parser class, used to parse: color names, strings, ints, hex ints and tuples into color tuples
    """

    @classmethod
    def parse(cls, color) -> Tuple[int, int, int]:
        """
        parses the string, int, or hex colors into color tuples

        raises:
            ValueError when passed an invalid color
        """
        from .color import Color

        if isinstance(color, str) and next((True for c in SupportedColors if c.name == color.upper()), False):
            color = cls._parse_color_name(color)

        elif isinstance(color, str) and not any(c not in string.hexdigits+"#" for c in color):
            color = cls._parse_hex_string(color)

        elif isinstance(color, int):
            color = cls._parse_int(color)

        elif isinstance(color, tuple):
            color = color

        elif isinstance(color, Color):
            color = color.r, color.g, color.b

        else:
            raise ValueError("{} is not a valid color!".format(color))

        return color

    @classmethod
    def _parse_color_name(cls, color: str) -> Tuple[int, int, int]:
        """parses named colors"""
        color = getattr(SupportedColors, color.upper())
        color = color.value
        return color

    @classmethod
    def _parse_hex_string(cls, color: str) -> Tuple[int, int, int]:
        if len(color) == 7 and color.startswith("#"):
            color = color.replace("#", "")

        color = tuple(int(color[i:i+2], 16) for i in range(0, 5, 2))

        return color

    @classmethod
    def _parse_int(cls, color: int) -> Tuple[int, int, int]:
        blue  = color % 256
        green = ((color - blue) // 256) % 256
        red   = ((color - blue) // 256 ** 2) - green // 256
        return red, green, blue

    @classmethod
    def _color_char(cls, color: Tuple[int, int, int]) -> str:
        return "\033[38;2;{0};{1};{2}m".format(*color)
