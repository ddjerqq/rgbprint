import sys
from typing import Any, Union, Tuple
from .parser import *
from .fore import Fore
from .color import Color
from .supported_colors import SUPPORTED_COLORS_LITERAL


__all__ = ["rgbprint"]


def rgbprint(
        *values: Any,
        color: Union[str, int, SUPPORTED_COLORS_LITERAL, Tuple[int, int, int], Color, None] = None,
        sep:   str = " ",
        end:   str = "\n") -> None:
    """
    print function with color support.
    -------------------------------------------------------------------------------------------------
    :param values: values to print, this can be Any type. each value is automatically cast to str.
    :param color: color name, color value as string, color hex integer, color tuple or rgbprint.Color object.
    :param sep: separator between values. gets automatically cast to str.
    :param end: end of line. gets automatically cast to str.
    """

    if color is not None:
        color = ColorParser.parse(color)
        color = Color(color)
        sys.stdout.write(str(color))

    text = sep.join(map(str, values))

    try:
        sys.stdout.write(text)
    finally:
        sys.stdout.write(end)
        sys.stdout.write(Fore.RESET)
