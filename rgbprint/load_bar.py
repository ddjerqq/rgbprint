import asyncio
import time

from .rgbprint import rgbprint
from .gradient import _gradient
from .color import Color
from .supported_colors import SUPPORTED_COLORS_LITERAL
from itertools import cycle
from typing import AsyncGenerator, Generator
from typing import Union, Tuple

__all__ = ["load_bar", "load_bar_async"]


async def load_bar_async(start_color: Union[str, int, SUPPORTED_COLORS_LITERAL, Tuple[int, int, int], Color],
                         end_color:   Union[str, int, SUPPORTED_COLORS_LITERAL, Tuple[int, int, int], Color],
                         /,
                         *,
                         width: int = 20,
                         delay: float = 0.5,
                         fill: str = "-",
                         delimeter: str = "█",
                         border_color: Union[str, int, SUPPORTED_COLORS_LITERAL, Tuple[int, int, int], Color] = "white"
                         ) -> AsyncGenerator:
    """
    async generator that prints a load bar with gradients! \n
    usage: \n
    >>> async for i in load_bar_async(Color("red"), Color("green"), width=30, delay=0.1):
    >>>     ...
    :param start_color:  the start color of the gradient
    :param end_color:    the end color of the gradient
    :param width:        the width of the load bar
    :param delay:        the delay between each tick
    :param fill:         the fill character
    :param delimeter:    the delimeter character
    :param border_color: the border color
    """
    start_color = Color(start_color)
    end_color = Color(end_color)

    delimeter = str(delimeter)
    fill = str(fill)

    gradient = _gradient((start_color.r, start_color.g, start_color.b),
                         (end_color.r, end_color.g, end_color.b),
                         width)

    gradient = cycle(gradient)

    for progress in range(width + 1):
        rgbprint("[", color=border_color, sep="", end="")
        content = f"{delimeter * int(progress)}{fill * (width - int(progress))}"

        for bar in content:
            rgbprint(bar, color=next(gradient), sep="", end="")

        rgbprint("]", color=border_color, sep="", end="\r")

        await asyncio.sleep(delay)
        yield
    print()


def load_bar(start_color: Union[str, int, SUPPORTED_COLORS_LITERAL, Tuple[int, int, int], Color],
             end_color:   Union[str, int, SUPPORTED_COLORS_LITERAL, Tuple[int, int, int], Color],
             /,
             *,
             width: int = 20,
             delay: float = 0.5,
             fill: str = "-",
             delimeter: str = "█",
             border_color: Union[str, int, SUPPORTED_COLORS_LITERAL, Tuple[int, int, int], Color] = "white"
             ) -> Generator:
    """
    generator that prints a load bar with gradients! \n
    usage: \n
    >>> for i in load_bar(Color("red"), Color("green"), width=30, delay=0.1):
    >>>     ...
    :param start_color:  the start color of the gradient
    :param end_color:    the end color of the gradient
    :param width:        the width of the load bar
    :param delay:        the delay between each tick
    :param fill:         the fill character
    :param delimeter:    the delimeter character
    :param border_color: the border color
    """
    start_color = Color(start_color)
    end_color = Color(end_color)

    delimeter = str(delimeter)
    fill = str(fill)

    gradient = _gradient((start_color.r, start_color.g, start_color.b),
                         (end_color.r, end_color.g, end_color.b),
                         width)

    gradient = cycle(gradient)

    for progress in range(width + 1):
        rgbprint("[", color=border_color, sep="", end="")
        content = f"{delimeter * int(progress)}{fill * (width - int(progress))}"

        for bar in content:
            rgbprint(bar, color=next(gradient), sep="", end="")

        rgbprint("]", color=border_color, sep="", end="\r")

        time.sleep(delay)
        yield
    print()
