import sys
from typing import Any
from typing import Optional

from .color import Color

__all__ = ["rgbprint"]


def rgbprint(
        *values: Any,
        color: Optional[Color] = None,
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
        sys.stdout.write(str(color))

    text = str(sep).join(map(str, values))

    try:
        sys.stdout.write(text)
    finally:
        sys.stdout.write(str(end))
        sys.stdout.write(Color.reset)
