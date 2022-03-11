"""
This is supposed to be a replacement for print, with support for
kwarg color \n
>>> from rgbprint import rgbprint as print
>>> from rgbprint import Colors
>>> print("Hello world", Colors.RED)
>>> print("lorem ipsum", "dolor sit amet", end="_", sep="$", color=0x00ff00)
>>> print("lorem ipsum", color="red")
>>> print("lorem ipsum", color=Colors.random())
>>> print("lorem ipsum", color=Colors.random(range(127), range(127, 255), range(127, 255))) \n
made by @ddjerqq.
"""

import os
import sys
import random
from typing import Any


os.system("")


class Colors:
    """
    The struct for default colors. \n
    >>> Colors.RED
    >>> Colors.BLUE
    >>> Colors.supported()
    >>> Colors.random()
    >>> Colors.random(range(127), range(127, 255), range(127, 255))
    """
    @staticmethod
    def random(
            red_range: range | None = None,
            green_range: range | None = None,
            blue_range: range | None = None
            ) -> [int, int, int]:
        """
        Get a random color. supports custom ranges. \n
        >>> Colors.random()
        >>> Colors.random(red_range=range(127, 255), green_range=range(0, 127))
        >>> Colors.random(range(127, 255), range(0, 127), range(0, 50)) \n
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        :param red_range:   range of red
        :param green_range: range of green
        :param blue_range:  range of blue
        :return: tuple of (red, green, blue)
        :raises: ValueError if range is out of range 0-255
        """

        min_red = 0
        max_red = 255
        min_green = 0
        max_green = 255
        min_blue = 0
        max_blue = 255

        if red_range is not None and isinstance(red_range, range):
            min_red, max_red = min(red_range), max(red_range)
            if min_red < 0 or max_red > 255:
                raise ValueError(f"red {min_red}-{max_red} out of range of 0-255")

        if green_range is not None and isinstance(green_range, range):
            min_green, max_green = min(green_range), max(green_range)
            if min_green < 0 or max_green > 255:
                raise ValueError(f"green {min_green}-{max_green} out of range of 0-255")

        if blue_range is not None and isinstance(blue_range, range):
            min_blue, max_blue = min(blue_range), max(blue_range)
            if min_blue < 0 or max_blue > 255:
                raise ValueError(f"blue {min_blue}-{max_blue} out of range of 0-255")

        color = (
            random.randint(min_red, max_red),
            random.randint(min_green, max_green),
            random.randint(min_blue, max_blue)
        )

        return color

    @staticmethod
    def supported() -> None:
        """
        print the supported colors. \n
        >>> Colors.supported()
        """
        print("Supported colors:")
        for idx, color in enumerate(Colors.SUPPORTED_COLORS):
            if not idx % 3:
                print("")
            rgbprint(f"{color.lower():<15}", end="", color=color)

    SUPPORTED_COLORS = [
        "RED",
        "LIGHT_RED",
        "DARK_RED",
        "GREEN",
        "LIGHT_GREEN",
        "DARK_GREEN",
        "BLUE",
        "LIGHT_BLUE",
        "DARK_BLUE",
        "YELLOW",
        "LIGHT_YELLOW",
        "DARK_YELLOW",
        "CYAN",
        "LIGHT_CYAN",
        "DARK_CYAN",
        "MAGENTA",
        "LIGHT_MAGENTA",
        "DARK_MAGENTA",
        "WHITE",
        "LIGHT_GRAY",
        "GRAY",
        "DARK_GRAY",
        "BLACK"
    ]

    RED  = (255, 0, 0)
    LIGHT_RED = (255, 128, 128)
    DARK_RED = (128, 0, 0)

    GREEN = (0, 255, 0)
    LIGHT_GREEN = (128, 255, 128)
    DARK_GREEN = (0, 128, 0)

    BLUE = (0, 0, 255)
    LIGHT_BLUE = (128, 128, 255)
    DARK_BLUE = (0, 0, 128)

    YELLOW = (255, 255, 0)
    LIGHT_YELLOW = (255, 255, 128)
    DARK_YELLOW = (128, 128, 0)

    CYAN = (0, 255, 255)
    LIGHT_CYAN = (128, 255, 255)
    DARK_CYAN = (0, 128, 128)

    MAGENTA = (255, 0, 255)
    LIGHT_MAGENTA = (255, 128, 255)
    DARK_MAGENTA = (128, 0, 128)

    WHITE = (255, 255, 255)
    GRAY = (128, 128, 128)
    BLACK = (0, 0, 0)

    LIGHT_GRAY = (192, 192, 192)
    DARK_GRAY = (64, 64, 64)



def rgbprint(
        *values: Any,
        color: str | int | tuple[int, int, int] | None = None,
        sep: str = " ",
        end: str = "\n",
        flush: bool = False) -> None:
    """
    print function with color support.
    ----------------------------------
    Made by @ddjerqq \n
    -------------------------------------------------------------------------------------------------
    :param values: values to print, this can be Any type. each value is automatically cast to str.
    :param color: default to None.
    :param color: str of the hex value of the color in rgb. either "ff00ff" or "#ff00ff"
    :param color: int of the hex value of the color. 0xff00ff
    :param color: tuple
    :param sep: separator between values.
    :param end: end of line.
    :param flush: flush the buffer or not.
    :return: None.
    :raises: TypeError when passed wrong parameters.
    :raises: ValueError if any value of the color is not in range 0-255.
    """

    if color is not None and not isinstance(color, (str, int, tuple)):
        raise TypeError(f"color should be str, int or tuple[int, int, int], not '{type(color).__name__}'")

    if color is not None and isinstance(color, str):
        if color.upper() in Colors.SUPPORTED_COLORS:
            color = getattr(Colors, color.upper())
        elif color.isalpha() and color not in Colors.SUPPORTED_COLORS:
            raise ValueError(f"color '{color}' is not supported. (see Color.supported())")
        elif len(color) == 7 and color[0] == "#":
            color = color[1:]
        elif len(color) != 6:
            raise TypeError("color must be a 6 or 7 digit hex value or a supported color (see Color.supported())")

        if not isinstance(color, tuple):
            try:
                color = int(color, 16)
            except ValueError:
                raise ValueError(f"color must be a 6 or 7 digit hex value of the color. not {color}")

    if color is not None and isinstance(color, int):
        blue  = color % 256
        green = ((color - blue) // 256) % 256
        red   = ((color - blue) // 256 ** 2) - green // 256
        color = red, green, blue

    if color is not None and isinstance(color, tuple) :
        for rgb in color:
            if not 0 <= rgb <= 255:
                raise ValueError(f"color tuple must have integer values 0-255. not {rgb}")


    if not isinstance(sep, str):
        raise TypeError(f"sep should be str, not '{type(sep).__name__}'")

    if not isinstance(end, str):
        raise TypeError(f"end should be str, not '{type(end).__name__}'")

    if not isinstance(flush, bool):
        raise TypeError(f"flush should be bool, not '{type(end).__name__}'")

    end_char = "\033[0m"
    if color is not None:
        color_character = f"\033[38;2;{color[0]};{color[1]};{color[2]}m"
        sys.stdout.write(color_character)

    try:
        for value in values:
            sys.stdout.write(str(value))
            sys.stdout.write(sep)
            if flush:
                sys.stdout.flush()

    except Exception as exc:
        sys.stdout.write(type(exc).__name__)
        sys.stdout.write(str(exc))

    finally:
        sys.stdout.write(end)
        sys.stdout.write(end_char)


