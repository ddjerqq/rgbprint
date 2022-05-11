import asyncio
from .rgbprint import rgbprint
from .gradient import _gradient
from .color import Color
from itertools import cycle
from typing import AsyncGenerator


__all__ = ["load_bar"]


async def load_bar(start_color,
                   end_color,
                   /,
                   *,
                   width=20,
                   delay=1,
                   fill="-",
                   delimeter="█",
                   border_color="white") -> AsyncGenerator:
    """
    """
    start_color = Color(start_color)
    end_color = Color(end_color)

    gradient = _gradient((start_color.r, start_color.g, start_color.b),
                         (end_color.r, end_color.g, end_color.b),
                         width)

    gradient = cycle(gradient)

    for progress in range(width + 1):
        rgbprint("[", color=border_color, sep="", end="")
        content = f"{delimeter * int(progress)}{fill * (width - int(progress))}"

        for bar in content:
            color = Color(next(gradient))
            print(f"{color}{bar}", sep="", end="")

        rgbprint("]", color=border_color, sep="", end="\r")

        await asyncio.sleep(delay)
        yield
    print()
