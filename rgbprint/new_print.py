import sys
from typing import Any


def _print(
        *values: Any,
        color: str | int | tuple[int, int, int] | None = None,
        sep: str = " ",
        end: str = "\n",
        flush: bool = False) -> None:
    """
    print function with color support.
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Made by @ddjerqq \n

    >>> from rgbprint.new_print import _print as print
    >>> from rgbprint.colors import Colors
    >>> print("lorem ipsum", color="#ff00ff")
    >>> print("foo", "bar", "baz", color=0xff0000, sep="_", end="", flush=True)
    >>> print("dolor sit amed", color=Colors.RED)
    >>> print("dolor sit amed", color=Colors.random())
    >>> print("dolor sit amed", color=Colors.random(range(256), range(0, 127), range(127, 256)))

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
        if len(color) == 7:
            color = color[1:]
        if len(color) != 6:
            raise TypeError("color must be a 6 or 7 digit hex value")

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
