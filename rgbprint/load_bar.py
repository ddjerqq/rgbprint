import time

from .rgbprint import rgbprint
from .gradient import gradient
from .color import Color
from itertools import cycle
from typing import Generator
from typing import Union, Tuple

__all__ = ["load_bar"]


def load_bar(start_color: Union[str, int, Tuple[int, int, int], Color],
             end_color:   Union[str, int, Tuple[int, int, int], Color],
             *,
             width: int   = 20,
             delay: float = 0.5,
             fill:  str   = " ",
             delimiter: str = "█",
             ) -> Generator:
    """
    generator that prints a load bar with gradients! \n
    raises:
        ValueError when passed an invalid color.
    ------------------------------------------------------
    :param start_color:  the start color of the gradient.
    :param end_color:    the end color of the gradient.
    :param width:        the width of the load bar.
    :param delay:        the delay between each tick.
    :param fill:         the fill character.
    :param delimiter:    the delimiter character.
    """
    start_color = Color(start_color)
    end_color   = Color(end_color)

    delimiter = str(delimiter)
    fill      = str(fill)

    grad      = cycle(gradient((start_color.r, start_color.g, start_color.b),
                               (end_color.r, end_color.g, end_color.b),
                               width))

    for progress in range(width + 1):
        rgbprint("[", color=Color((255, 255, 255)), sep="", end="")

        content = "{}{}".format(delimiter*progress, fill*(width-progress))

        for bar in content:
            rgbprint(bar, color=next(grad), sep="", end="")

        rgbprint("]", color=Color((255, 255, 255)), sep="", end="\r")
        time.sleep(delay)
        yield

    rgbprint()
