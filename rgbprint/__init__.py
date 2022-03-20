"""
RGBPRINT made by @ddjerqq.
--------------------------
rgb toolkit, for printing gradients rgb text and much more! \n
to see what this library allows you to do, just call        \n
>>> demo() \n
see: \n
>>> supported_colors()           \n
>>> random_color()               \n
>>> rgbprint()                   \n
>>> rgb_type()                   \n
>>> async_rgb_type()             \n
>>> gradient_print()             \n
>>> gradient_change()            \n
>>> async_gradient_change()      \n
>>> gradient_scroll()            \n
>>> async_gradient_scroll()      \n
>>> gradient_type()              \n
>>> async_gradient_type()        \n
"""

import os
import sys
import time
import random
import asyncio
from typing import Any

# init
os.system("")


# colors
RED           = (255, 000, 000)
LIGHT_RED     = (255, 128, 128)
DARK_RED      = (128, 000, 000)
GREEN         = (000, 255, 000)
LIGHT_GREEN   = (128, 255, 128)
DARK_GREEN    = (000, 128, 000)
BLUE          = (000, 000, 255)
LIGHT_BLUE    = (128, 128, 255)
DARK_BLUE     = (000, 000, 128)
YELLOW        = (255, 255, 000)
LIGHT_YELLOW  = (255, 255, 128)
CYAN          = (000, 255, 255)
LIGHT_CYAN    = (128, 255, 255)
DARK_CYAN     = (000, 128, 128)
DARK_YELLOW   = (128, 128, 000)
MAGENTA       = (255, 000, 255)
LIGHT_MAGENTA = (255, 128, 255)
DARK_MAGENTA  = (128, 000, 128)
WHITE         = (255, 255, 255)
GRAY          = (128, 128, 128)
BLACK         = (000, 000, 000)
LIGHT_GRAY    = (192, 192, 192)
DARK_GRAY     = ( 64,  64,  64)

END_CHAR = "\033[0m"

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


# protected
def _parse(color: str | int | tuple[int, int, int]) -> tuple[int, int, int]:
    """
    Parse the color and return tuple of rgb
    ---------------------------------------
    >>> _parse("#ff0000") -> (255, 0, 0)
    >>> _parse("red") -> (255, 0, 0)
    >>> _parse(0xff0000) -> (255, 0, 0)
    :param color:
    :return:
    """
    if color is not None and not isinstance(color, (str, int, tuple)):
        raise TypeError(f"color should be str, int or tuple[int, int, int], not '{type(color).__name__}'")

    if color is not None and isinstance(color, str):
        if color.upper() in SUPPORTED_COLORS:
            color = globals()[color.upper()]
        elif color.isalpha() and color not in SUPPORTED_COLORS:
            raise ValueError(f"color '{color}' is not supported. (see supported_colors())")
        elif len(color) == 7 and color[0] == "#":
            color = color[1:]
        elif len(color) != 6:
            raise TypeError("color must be a 6 or 7 digit hex value or a supported color (see supported_colors())")

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

    return color


def _gradient(start: tuple[int, int, int], end: tuple[int, int, int], steps: int) -> list[tuple[int, int, int]]:
    """
    get a gradient from the start and end colors.
    -----------------------------------------------
    get `steps` amount of colors from start to end.
    :param start: start color
    :param end: end color
    :param steps: int amount of steps, often len(txt)
    :return: list of color tuples
    """
    start = _parse(start)
    end = _parse(end)

    rs = [start[0]]
    gs = [start[1]]
    bs = [start[2]]
    for i in range(1, steps):
        rs.append(round(start[0] + (end[0] - start[0]) * i / steps))
        gs.append(round(start[1] + (end[1] - start[1]) * i / steps))
        bs.append(round(start[2] + (end[2] - start[2]) * i / steps))

    # print(*map(lambda i: f"{i:03}", rs))
    # print(*map(lambda i: f"{i:03}", gs))
    # print(*map(lambda i: f"{i:03}", bs))

    return list(zip(rs, gs, bs))


def _color_char(color: tuple[int, int, int]) -> str:
    """
    get printable color character from tuple of ints
    :param color: parsed tuple of ints
    :return: ansi escape character code for printing that rgb color
    """
    return f"\033[38;2;{color[0]};{color[1]};{color[2]}m"


# public
def demo():
    text = "Hello user, my name is ddjerqq. I made this library for you <3"
    time.sleep(2)

    print("supported colors:")
    supported_colors()

    rgbprint("\n\n\nrandom color demo", color=random_color())
    rgbprint("random color demo", color=random_color())
    rgbprint("random color demo", color=random_color())
    rgbprint("random color demo", color=random_color())
    rgbprint("random color demo", color=random_color())

    print('\nrgbprint(text, color="red")')
    rgbprint(text, color="red")

    print('\nrgb_type(text, color="red")')
    rgb_type(text, color="red")

    print('\ngradient_print(text, start_color="red", end_color="green")')
    gradient_print(text, start_color="red", end_color="green")

    print('\ngradient_change(text, start_color="red", end_color="green")')
    gradient_change(text, start_color="red", end_color="green")

    print('\ngradient_scroll(text, start_color="red", end_color="green", delay=0.05)')
    gradient_scroll(text, start_color="red", end_color="green", delay=0.05)

    print('\ngradient_scroll(text, start_color="red", end_color="green", delay=0.005, times=6)')
    gradient_scroll(text, start_color="red", end_color="green", delay=0.005, times=6)

    print('\ngradient_type(text, start_color="red", end_color="green")')
    gradient_type(text, start_color="red", end_color="green", delay=0.05)

    print("\ndo keep in mind, that async alternatives are also supported.")
    print("now go crazy, and show me what you come up with <3")


def supported_colors() -> None:
    """
    print the supported colors.
    """

    for idx, color in enumerate(SUPPORTED_COLORS):
        if not idx % 3:
            print("")
        rgbprint(f"{color.lower():<15}", end="", color=color)


def random_color(
        *,
        min_red: int = 0,
        max_red: int = 255,
        min_green: int = 0,
        max_green: int = 255,
        min_blue: int = 0,
        max_blue: int = 255
        ) -> tuple[int, int, int]:
    """
    Get a random color. supports custom ranges. \n
    >>> random_color()
    >>> random_color(red_range=range(127, 255), green_range=range(0, 127))
    >>> random_color(range(127, 255), range(0, 127), range(0, 50)) \n
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    :param min_red: red minimum, int
    :param max_red: red maximum, int
    :param min_green: green minimum, int
    :param max_green: green maximum, int
    :param min_blue: blue minimum, int
    :param max_blue: blue maximum, int
    :return: tuple of (red, green, blue)
    :raises: ValueError if range is out of range 0-255
    """
    if min_red < 0 or max_red > 255:
        raise ValueError(f"red {min_red}-{max_red} out of range of 0-255")
    if min_green < 0 or max_green > 255:
        raise ValueError(f"green {min_green}-{max_green} out of range of 0-255")
    if min_blue < 0 or max_blue > 255:
        raise ValueError(f"blue {min_blue}-{max_blue} out of range of 0-255")
    color = (
        random.randint(min_red, max_red),
        random.randint(min_green, max_green),
        random.randint(min_blue, max_blue)
    )
    return color


def rgbprint(
        *values: Any,
        color: str | int | tuple[int, int, int] | None = None,
        sep:   str = " ",
        end:   str = "\n",
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


    if not isinstance(sep, str):
        raise TypeError(f"sep should be str, not '{type(sep).__name__}'")

    if not isinstance(end, str):
        raise TypeError(f"end should be str, not '{type(end).__name__}'")

    if not isinstance(flush, bool):
        raise TypeError(f"flush should be bool, not '{type(end).__name__}'")

    if color is not None:
        color = _parse(color)
        sys.stdout.write(_color_char(color))

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
        sys.stdout.write(END_CHAR)


def rgb_type(
        *values: Any,
        color: str | int | tuple[int, int, int] | None = None,
        delay: float = 0.01,
        sep:   str = " ",
        end:   str = "\n") -> None:
    """
    same as rgbprint, but this one types the characters one by one, after the delay
    :param values: any value, will be auto-cast to str
    :param color: this can be any supported color, str int or tuple
    :param delay: float delay for each character. (recommended 0.01-0.05)
    :param sep: separator value, should be str
    :param end: end value, should be str
    :return: None
    """
    if color is not None:
        color = _parse(color)
        sys.stdout.write(_color_char(color))

    text = sep.join(map(str, values))

    for char in text:
        sys.stdout.write(char)
        time.sleep(delay)

    sys.stdout.write(end)
    sys.stdout.write(END_CHAR)
    sys.stdout.flush()


# async
async def async_rgb_type(
        *values: Any,
        color: str | int | tuple[int, int, int] | None = None,
        delay: float = 0.01,
        sep:   str = " ",
        end:   str = "\n") -> None:
    """
    async alternative to the rgb_type
    :param values: any value, will be auto-cast to str
    :param color: this can be any supported color, str int or tuple
    :param delay: float delay for each character. (recommended 0.01-0.05)
    :param sep: separator value, should be str
    :param end: end value, should be str
    :return: None
    """
    if color is not None:
        color = _parse(color)
        sys.stdout.write(_color_char(color))

    text = sep.join(map(str, values))

    for char in text:
        sys.stdout.write(char)
        await asyncio.sleep(delay)

    sys.stdout.write(end)
    sys.stdout.write(END_CHAR)
    sys.stdout.flush()


def gradient_print(
        *values: Any,
        start_color: str | int | tuple[int, int, int] | None = None,
        end_color:   str | int | tuple[int, int, int] | None = None,
        sep: str = " ",
        end: str = "\n") -> None:
    """
    print gradients lmao
    --------------------
    :param values: any value, will be auto-cast to str
    :param start_color: start color, this can be in any supported format
    :param end_color: end color, keep in mind, you should pass both start and end colors.
    :param sep: separator, must be str. default " "
    :param end: end must be str. default "\n"
    :return: None
    """

    if not isinstance(sep, str):
        raise TypeError(f"sep should be str, not '{type(sep).__name__}'")

    if not isinstance(end, str):
        raise TypeError(f"end should be str, not '{type(end).__name__}'")

    text = sep.join(map(str, values)) + end

    gradient = None
    if start_color is not None and end_color is not None:
        start_color = _parse(start_color)
        end_color   = _parse(end_color)
        gradient    = _gradient(start_color, end_color, len(text))

    for idx, char in enumerate(text):
        if gradient:
            sys.stdout.write(_color_char(gradient[idx]))
        sys.stdout.write(char)
    else:
        sys.stdout.write(END_CHAR)
        sys.stdout.flush()


def gradient_change(
        *values: Any,
        start_color: str | int | tuple[int, int, int] | None = None,
        end_color:   str | int | tuple[int, int, int] | None = None,
        delay: float = 0.05,
        sep: str = " ",
        end: str = "\n") -> None:
    """
    print gradients and change in place from red to green in same place
    -------------------------------------------------------------------
    :param values: any value, will be auto-cast to str
    :param start_color: start color, this can be in any supported format
    :param end_color: end color. keep in mind, you should pass both start and end colors.
    :param delay: time to sleep between changing gradients
    :param sep: separator, must be str. default " "
    :param end: end must be str. default "\n"
    :return: None
    """

    if not isinstance(sep, str):
        raise TypeError(f"sep should be str, not '{type(sep).__name__}'")

    if not isinstance(end, str):
        raise TypeError(f"end should be str, not '{type(end).__name__}'")

    text = sep.join(map(str, values))

    gradient = None
    if start_color is not None and end_color is not None:
        start_color = _parse(start_color)
        end_color   = _parse(end_color)
        gradient    = _gradient(start_color, end_color, len(text))

    for idx in range(len(text)):
        if gradient:
            sys.stdout.write(_color_char(gradient[idx]))
        sys.stdout.write("\r" + text)
        time.sleep(delay)
    else:
        sys.stdout.write(end)
        sys.stdout.write(END_CHAR)
        sys.stdout.flush()


# async
async def async_gradient_change(
        *values: Any,
        start_color: str | int | tuple[int, int, int] | None = None,
        end_color:   str | int | tuple[int, int, int] | None = None,
        delay: float = 0.05,
        sep: str = " ",
        end: str = "\n") -> None:
    """
    async alternative of the gradient_change
    -------------------------------------------------------------------
    :param values: any value, will be auto-cast to str
    :param start_color: start color, this can be in any supported format
    :param end_color: end color. keep in mind, you should pass both start and end colors.
    :param delay: time to sleep between changing gradients
    :param sep: separator, must be str. default " "
    :param end: end must be str. default "\n"
    :return: None
    """

    if not isinstance(sep, str):
        raise TypeError(f"sep should be str, not '{type(sep).__name__}'")

    if not isinstance(end, str):
        raise TypeError(f"end should be str, not '{type(end).__name__}'")

    text = sep.join(map(str, values))

    gradient = None
    if start_color is not None and end_color is not None:
        start_color = _parse(start_color)
        end_color   = _parse(end_color)
        gradient    = _gradient(start_color, end_color, len(text))

    for idx in range(len(text)):
        if gradient:
            sys.stdout.write(_color_char(gradient[idx]))
        sys.stdout.write("\r" + text)
        await asyncio.sleep(delay)
    else:
        sys.stdout.write(end)
        sys.stdout.write(END_CHAR)
        sys.stdout.flush()


def gradient_scroll(
        *values: Any,
        start_color: str | int | tuple[int, int, int] | None = None,
        end_color:   str | int | tuple[int, int, int] | None = None,
        delay: float = 0.03,
        times: int = 4,
        reverse: bool = False,
        sep: str = " ",
        end: str = "\n") -> None:
    """
    scroll colors, in place. you should try this one for sure.
    -------------------------------------------------------------------
    :param values: any value, will be auto-cast to str
    :param start_color: start color, this can be in any supported format
    :param end_color: end color. keep in mind, you should pass both start and end colors.
    :param delay: time to sleep between changing gradients, (suggested from 0.01-0.05)
    :param times: how many times to scroll through the text
    :param reverse: scroll from right to left when True.
    :param sep: separator, must be str. default " "
    :param end: end must be str. default "\n"
    :return: None
    """

    if not isinstance(sep, str):
        raise TypeError(f"sep should be str, not '{type(sep).__name__}'")

    if not isinstance(end, str):
        raise TypeError(f"end should be str, not '{type(end).__name__}'")

    text = sep.join(map(str, values))
    if len(text) % 2:
        text += sep

    gradient = None
    if start_color is not None and end_color is not None:
        start_color = _parse(start_color)
        end_color   = _parse(end_color)
        first_half  = _gradient(start_color, end_color, len(text) // 2)
        second_half = _gradient(end_color, start_color, len(text) // 2)
        gradient    = first_half + second_half


    for _ in range(times * len(text)):
        gradient.append(gradient.pop()) if reverse else gradient.insert(0, gradient.pop())

        for idx, char in enumerate(gradient):
            sys.stdout.write(_color_char(char))
            sys.stdout.write(text[idx])
        sys.stdout.write("\r")
        time.sleep(delay)

    sys.stdout.write(end)
    sys.stdout.write(END_CHAR)
    sys.stdout.flush()


# async
async def async_gradient_scroll(
        *values: Any,
        start_color: str | int | tuple[int, int, int] | None = None,
        end_color:   str | int | tuple[int, int, int] | None = None,
        delay: float = 0.03,
        times: int = 4,
        reverse: bool = False,
        sep: str = " ",
        end: str = "\n") -> None:
    """
    asnyc alternative of the gradient_scroll
    -------------------------------------------------------------------
    :param values: any value, will be auto-cast to str
    :param start_color: start color, this can be in any supported format
    :param end_color: end color. keep in mind, you should pass both start and end colors.
    :param delay: time to sleep between changing gradients, (suggested from 0.01-0.05)
    :param times: how many times to scroll through the text
    :param reverse: scroll from right to left when True.
    :param sep: separator, must be str. default " "
    :param end: end must be str. default "\n"
    :return: None
    """

    if not isinstance(sep, str):
        raise TypeError(f"sep should be str, not '{type(sep).__name__}'")

    if not isinstance(end, str):
        raise TypeError(f"end should be str, not '{type(end).__name__}'")

    text = sep.join(map(str, values))
    if len(text) % 2:
        text += sep

    gradient = None
    if start_color is not None and end_color is not None:
        start_color = _parse(start_color)
        end_color   = _parse(end_color)
        first_half  = _gradient(start_color, end_color, len(text) // 2)
        second_half = _gradient(end_color, start_color, len(text) // 2)
        gradient    = first_half + second_half


    for _ in range(times * len(text)):
        gradient.append(gradient.pop()) if reverse else gradient.insert(0, gradient.pop())

        for idx, char in enumerate(gradient):
            sys.stdout.write(_color_char(char))
            sys.stdout.write(text[idx])
        sys.stdout.write("\r")
        await asyncio.sleep(delay)

    sys.stdout.write(end)
    sys.stdout.write(END_CHAR)
    sys.stdout.flush()



def gradient_type(
        *values: Any,
        start_color: str | int | tuple[int, int, int] | None = None,
        end_color:   str | int | tuple[int, int, int] | None = None,
        delay: float = 0.03,
        sep: str = " ",
        end: str = "\n") -> None:
    """
    typewriter, type each character one by one, with some delay
    ----------------
    :param values: any value, will be auto-cast to str
    :param start_color: start color, this can be in any supported format
    :param end_color: end color. keep in mind, you should pass both start and end colors.
    :param delay: time to sleep between changing gradients, (suggested from 0.01-0.05)
    :param sep: separator, must be str. default " "
    :param end: end must be str. default "\n"
    :return: None
    """
    if not isinstance(sep, str):
        raise TypeError(f"sep should be str, not '{type(sep).__name__}'")

    if not isinstance(end, str):
        raise TypeError(f"end should be str, not '{type(end).__name__}'")

    text = sep.join(map(str, values))

    gradient = None
    if start_color is not None and end_color is not None:
        start_color = _parse(start_color)
        end_color = _parse(end_color)
        gradient = _gradient(start_color, end_color, len(text))

    for idx, char in enumerate(text):
        sys.stdout.write(_color_char(gradient[idx]))
        sys.stdout.write(char)
        time.sleep(delay)

    sys.stdout.write(end)
    sys.stdout.write(END_CHAR)
    sys.stdout.flush()


# async
async def async_gradient_type(
        *values: Any,
        start_color: str | int | tuple[int, int, int] | None = None,
        end_color:   str | int | tuple[int, int, int] | None = None,
        delay: float = 0.03,
        sep: str = " ",
        end: str = "\n") -> None:
    """
    async alternative to gradient_type
    ----------------
    :param values: any value, will be auto-cast to str
    :param start_color: start color, this can be in any supported format
    :param end_color: end color. keep in mind, you should pass both start and end colors.
    :param delay: time to sleep between changing gradients, (suggested from 0.01-0.05)
    :param sep: separator, must be str. default " "
    :param end: end must be str. default "\n"
    :return: None
    """
    if not isinstance(sep, str):
        raise TypeError(f"sep should be str, not '{type(sep).__name__}'")

    if not isinstance(end, str):
        raise TypeError(f"end should be str, not '{type(end).__name__}'")

    text = sep.join(map(str, values))

    gradient = None
    if start_color is not None and end_color is not None:
        start_color = _parse(start_color)
        end_color = _parse(end_color)
        gradient = _gradient(start_color, end_color, len(text))

    for idx, char in enumerate(text):
        sys.stdout.write(_color_char(gradient[idx]))
        sys.stdout.write(char)
        await asyncio.sleep(delay)

    sys.stdout.write(end)
    sys.stdout.write(END_CHAR)
    sys.stdout.flush()


if __name__ == "__main__":
    demo()
