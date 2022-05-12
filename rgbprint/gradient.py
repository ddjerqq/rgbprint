import asyncio
import sys
import time
from typing import Tuple, List, Any, Union


from .color import Color
from .parser import ColorParser
from .fore import Fore
from .supported_colors import SUPPORTED_COLORS_LITERAL


__all__ = ["gradient_print", "gradient_change", "gradient_scroll", "gradient_scroll_async"]


def _gradient(start, end, steps) -> List[tuple[int, int, int]]:
    rs = [start[0]]
    gs = [start[1]]
    bs = [start[2]]
    for i in range(1, steps):
        rs.append(round(start[0] + (end[0] - start[0]) * i / steps))
        gs.append(round(start[1] + (end[1] - start[1]) * i / steps))
        bs.append(round(start[2] + (end[2] - start[2]) * i / steps))

    return list(zip(rs, gs, bs))


def gradient_print(
        *values: Any,
        start_color: Union[str, int, Tuple[int, int, int], Color, SUPPORTED_COLORS_LITERAL],
        end_color:   Union[str, int, Tuple[int, int, int], Color, SUPPORTED_COLORS_LITERAL],
        sep: str = " ",
        end: str = "\n",
        top_to_bottom: bool = False) -> None:
    """
    print gradients lmao
    --------------------
    :param values: any value, will be auto-cast to str
    :param start_color: start color, this can be in any supported format
    :param end_color: end color, keep in mind, you should pass both start and end colors.
    :param sep: separator, gets auto-cast to str
    :param end: end char, gets auto-cast to str
    :param top_to_bottom: if True, will print the gradient from top to bottom, otherwise from left to right.
    """

    sep = str(sep)
    text = sep.join(map(str, values))

    start_color = ColorParser.parse(start_color)
    end_color   = ColorParser.parse(end_color)
    multiline   = "\n" in text and not top_to_bottom

    if multiline:
        text = text.split("\n")

    steps = len(max(text)) if multiline else len(text)

    gradient = _gradient(start_color, end_color, steps)

    try:
        if multiline:
            for row in text:
                for i, char in enumerate(row):
                    color = gradient[i]
                    sys.stdout.write(str(Color(color)))
                    sys.stdout.write(char)
                    sys.stdout.flush()
                sys.stdout.write("\n")
            sys.stdout.write(Fore.RESET)
            sys.stdout.flush()
        else:
            for i, char in enumerate(text):
                color = gradient[i]
                sys.stdout.write(str(Color(color)))
                sys.stdout.write(char)
                sys.stdout.flush()
        sys.stdout.write(end)
    finally:
        sys.stdout.write(Fore.RESET)
        sys.stdout.flush()


def gradient_change(
        *values: Any,
        start_color: Union[str, int, Tuple[int, int, int], Color, SUPPORTED_COLORS_LITERAL],
        end_color:   Union[str, int, Tuple[int, int, int], Color, SUPPORTED_COLORS_LITERAL],
        delay: float = 0.05,
        sep: str = " ",
        end: str = "\n") -> None:
    """
    print gradients and change in place from start_color to end_color in same place \n
    NOTE: this DOES NOT work with multiline strings. \n
    --------------------------------------------------------------------------------
    :param values: any value, will be auto-cast to str
    :param start_color: start color, this can be in any supported format
    :param end_color: end color, keep in mind, you should pass both start and end colors.
    :param delay: delay between each change, recommeneded to be lower than 0.1
    :param sep: separator, gets auto-cast to str
    :param end: end char, gets auto-cast to str
    """

    sep = str(sep)
    text = sep.join(map(str, values))

    start_color = ColorParser.parse(start_color)
    end_color   = ColorParser.parse(end_color)
    steps       = len(text)
    gradient    = _gradient(start_color, end_color, steps)

    try:
        for idx in range(steps):
            sys.stdout.write(str(Color(gradient[idx])))
            sys.stdout.write("\r" + text)
            sys.stdout.flush()
            time.sleep(delay)
        sys.stdout.flush()
        sys.stdout.write(end)
    finally:
        sys.stdout.write(Fore.RESET)
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
    scroll gradients XD \n
    NOTE: this DOES NOT work with multiline strings. \n
    --------------------
    :param values: any value, will be auto-cast to str
    :param start_color: start color, this can be in any supported format
    :param end_color: end color, keep in mind, you should pass both start and end colors.
    :param delay: delay between each change, recommeneded to be lower than 0.1
    :param times: number of times to scroll
    :param reverse: reverse the gradient
    :param sep: separator, gets auto-cast to str
    :param end: end char, gets auto-cast to str
    """
    sep = str(sep)
    text = sep.join(map(str, values))
    if len(text) % 2:
        text += " "

    start_color = ColorParser.parse(start_color)
    end_color   = ColorParser.parse(end_color)
    steps       = len(text)

    first_half  = _gradient(start_color, end_color, steps // 2)
    second_half = _gradient(end_color, start_color, steps // 2)
    gradient    = first_half + second_half

    try:
        for _ in range(times * steps):
            gradient.append(gradient.pop()) if reverse else gradient.insert(0, gradient.pop())

            for idx, char in enumerate(gradient):
                sys.stdout.write(str(Color(char)))
                sys.stdout.write(text[idx])
                sys.stdout.flush()
            sys.stdout.write("\r")
            sys.stdout.flush()
            time.sleep(delay)

        sys.stdout.write(end)
    finally:
        sys.stdout.write(Fore.RESET)
        sys.stdout.flush()


# async
async def gradient_scroll_async(
        *values: Any,
        start_color: str | int | tuple[int, int, int] | None = None,
        end_color:   str | int | tuple[int, int, int] | None = None,
        delay: float = 0.03,
        times: int = 4,
        reverse: bool = False,
        sep: str = " ",
        end: str = "\n") -> None:
    """
    scroll gradients asynchronously \n
    NOTE: this DOES NOT work with multiline strings. \n
    --------------------
    :param values: any value, will be auto-cast to str
    :param start_color: start color, this can be in any supported format
    :param end_color: end color, keep in mind, you should pass both start and end colors.
    :param delay: delay between each change, recommeneded to be lower than 0.1
    :param times: number of times to scroll
    :param reverse: reverse the gradient
    :param sep: separator, gets auto-cast to str
    :param end: end char, gets auto-cast to str
    """
    sep = str(sep)
    text = sep.join(map(str, values))
    if len(text) % 2:
        text += " "

    start_color = ColorParser.parse(start_color)
    end_color   = ColorParser.parse(end_color)
    steps  = len(max(text))

    first_half  = _gradient(start_color, end_color, steps // 2)
    second_half = _gradient(end_color, start_color, steps // 2)
    gradient    = first_half + second_half

    try:
        for _ in range(times * len(text)):
            gradient.append(gradient.pop()) if reverse else gradient.insert(0, gradient.pop())

            for idx, char in enumerate(gradient):
                sys.stdout.write(str(Color(char)))
                sys.stdout.write(text[idx])
                sys.stdout.flush()
            sys.stdout.write("\r")
            sys.stdout.flush()
            await asyncio.sleep(delay)

        sys.stdout.write(end)
    finally:
        sys.stdout.write(Fore.RESET)
        sys.stdout.flush()
