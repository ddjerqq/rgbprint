from typing import Tuple
from typing import Union


from .supported_colors import SupportedColors, SUPPORTED_COLORS_LITERAL


__all__ = ["ColorParser"]


class ColorParser:
    """
    the color parser class, used to parse: color names, strings, ints, hex ints and tuples into color tuples
    """

    @classmethod
    def parse(cls, color) -> Union[Tuple[int, int, int], None]:
        """parses the color"""
        from .color import Color

        if isinstance(color, str) and hasattr(SupportedColors, color.upper()):
            color = cls._parse_color_name(color)

        elif isinstance(color, str):
            color = cls._parse_hex_string(color)

        elif isinstance(color, int):
            color = cls._parse_int(color)

        elif isinstance(color, tuple):
            color = color

        elif isinstance(color, Color):
            color = color.r, color.g, color.b

        else:
            return None

        color = cls._clip_color_tuple(color)

        return color

    @classmethod
    def _clip_color_tuple(cls, color: Tuple[int, int, int]) -> Tuple:
        return tuple(max(0, min(x, 255)) for x in list(color))

    @classmethod
    def _parse_color_name(cls, color: Union[str, SUPPORTED_COLORS_LITERAL]) -> Tuple[int, int, int]:
        """parses named colors"""
        color = getattr(SupportedColors, color.upper())
        color = color.value
        return color

    @classmethod
    def _parse_hex_string(cls, color: str) -> Tuple:
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
    def _color_char(cls, color: Union[str, Tuple, int]) -> str:
        return f"\033[38;2;{color[0]};{color[1]};{color[2]}m"
