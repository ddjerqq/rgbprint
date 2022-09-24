from __future__ import annotations

import sys
from typing import (
    Any,
    Optional,
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    from . import ColorType

from .color import Color


def rgbprint(
    *values: Any, color: Optional[ColorType] = None, sep: str = " ", end: str = "\n"
) -> None:
    """print but with color keyword argument support.

    Prints the values to sys.stdout.

    >>> rgbprint("value", sep=' ', end='end', color=None)

    Args:
        *values (Any): *values to print.
        color (ColorType): `optional` color. see examples down below for supported formats.
        sep (:obj:`str`, optional): optional, string inserted between values, default a space.
        end (:obj:`str`, optional): optional, string appended after the last value, default a newline.

    Examples:
        >>> user = "john smith"
        >>> rgbprint("welcome", user, "you are", 25, "years old", color=Color.forest_green)
        >>> rgbprint(*["orange", "apple", "banana"], sep="_", color="yellow")

        >>> # all supported color formats
        >>> rgbprint("hello", color="red")
        >>> rgbprint("hello", color=0xff00ff)
        >>> rgbprint("hello", color="#ff00ff")
        >>> rgbprint("hello", color="ff00ff")
        >>> rgbprint("hello", color=[255, 0, 255])
        >>> rgbprint("hello", color=(255, 0, 255))
        >>> rgbprint("hello", color=(255, 0, 0xFF))
        >>> rgbprint("hello", color=Color.red)
        >>> rgbprint("hello", color=Color.random)

    Raises:
        ValueError: if the color is in an unsupported format, or is out of range of 0-16777215 (0x000000-0xFFFFFF).
        TypeError: if the color is of unsupported type.
    """

    if color is not None:
        # colorify non-color types
        # such as strings, ints, and tuples.
        color = Color(color)
        sys.stdout.write(str(color))

    text = str(sep).join(map(str, values))

    try:
        sys.stdout.write(text)
        sys.stdout.write(str(end))
    finally:
        sys.stdout.write(Color.reset)
