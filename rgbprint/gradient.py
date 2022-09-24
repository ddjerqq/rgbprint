from __future__ import annotations

import asyncio
import sys
import time
from typing import Tuple, List, Any, TYPE_CHECKING

from .color import Color

if TYPE_CHECKING:
    from . import ColorType


def gradient(
    start: Tuple[int, int, int], end: Tuple[int, int, int], steps: int
) -> List[Tuple[int, int, int]]:
    """
    Generate a gradient, from the start color to the end color with `steps` amount.

    Args:
        start (tuple[int, int, int]): start color, this must be a tuple of 3 ints.
        end (tuple[int, int, int]): end color, this must be a tuple of 3 ints.
        steps (int): amount of steps.

    Returns:
        list[tuple[int, int, int]]: `steps` amount of colors in between the `start_color` and the `end_color`
    """
    rs: List[int] = [start[0]]
    gs: List[int] = [start[1]]
    bs: List[int] = [start[2]]

    for step in range(1, steps):
        rs.append(round(start[0] + (end[0] - start[0]) * step / steps))
        gs.append(round(start[1] + (end[1] - start[1]) * step / steps))
        bs.append(round(start[2] + (end[2] - start[2]) * step / steps))

    return list(
        zip(
            rs,  # [255, 127,   0]
            gs,  # [0,   127, 255]
            bs,  # [0,     0,   0]
        )
    )


def gradient_print(
    *values: Any,
    start_color: ColorType,
    end_color: ColorType,
    sep: str = " ",
    end: str = "\n",
) -> None:
    """
    print gradients on your terminal

    Args:
        *values (Any): *values to print.
        start_color (ColorType): start_color. see examples down below for supported formats.
        end_color (ColorType): end_color. see examples down below for supported formats.
        sep (:obj:`str`, optional): optional, string inserted between values, default a space.
        end (:obj:`str`, optional): optional, string appended after the last value, default a newline.

    Examples:
        >>> from rgbprint import gradient_print, Color
        >>> username = "john doe"
        >>> gradient_print("hello", start_color="red", end_color="yellow")
        >>> gradient_print("hello", username, "welcome to the app", start_color=Color.forest_green, end_color=0xFF00FF)
        >>> gradient_print("[+] loading data, please wait...", start_color=Color.aqua_marine, end_color=Color.peach_puff)

    Raises:
        ValueError: if the color is in an unsupported format, or is out of range of 0-16777215 (0x000000-0xFFFFFF).
        TypeError: if the color is of unsupported type, or the function is missing arguments.
    """
    text = str(sep).join(map(str, values))

    start_color = tuple(Color(start_color))
    end_color = tuple(Color(end_color))

    steps = len(text)

    grad = gradient(start_color, end_color, steps)

    try:
        for i, char in enumerate(text):
            color = grad[i]
            sys.stdout.write(str(Color(color)) + char)
        sys.stdout.write(str(end))
    finally:
        sys.stdout.write(Color.reset)
        sys.stdout.flush()


def gradient_change(
    *values: Any,
    start_color: ColorType,
    end_color: ColorType,
    delay: float = 0.03,
    times: int = 1,
    reverse: bool = False,
    sep: str = " ",
    end: str = "\n",
) -> None:
    """
    change gradients in place on your terminal

    Args:
        *values (Any): *values to print.
        start_color (ColorType): start_color. see examples down below for supported formats.
        end_color (ColorType): end_color. see examples down below for supported formats.
        delay (float, optional): optional, the delay between the change of the gradient, recommended range: .05 - .1
        times (int, optional): optional, the amount of times to change the gradient in place.
        reverse (bool, optional): whether to start with the end color or not.
        sep (:obj:`str`, optional): optional, string inserted between values, default a space.
        end (:obj:`str`, optional): optional, string appended after the last value, default a newline.

    Examples:
        >>> from rgbprint import gradient_change, Color
        >>> username = "john doe"
        >>> gradient_change("hello", start_color="red", end_color="yellow")
        >>> gradient_change("hello", username, "welcome to the app", start_color=Color.forest_green, end_color=0xFF00FF)
        >>> gradient_change("[+] loading data, please wait...", start_color="red", end_color="blue", times=10, delay=.1)

    Raises:
        ValueError: if the color is in an unsupported format, or is out of range of 0-16777215 (0x000000-0xFFFFFF).
        TypeError: if the color is of unsupported type, or the function is missing arguments.
    """

    text = str(sep).join(map(str, values))

    start_color = tuple(Color(start_color))
    end_color = tuple(Color(end_color))
    steps = len(text)
    grad = gradient(start_color, end_color, steps)

    if reverse:
        grad.reverse()

    try:
        for _ in range(times):
            for idx in range(steps):
                sys.stdout.write(str(Color(grad[idx])) + "\r" + text)
                sys.stdout.flush()
                time.sleep(delay)
            sys.stdout.flush()
    finally:
        sys.stdout.write(end)
        sys.stdout.write(Color.reset)
        sys.stdout.flush()


def gradient_scroll(
    *values: Any,
    start_color: ColorType,
    end_color: ColorType,
    delay: float = 0.03,
    times: int = 4,
    reverse: bool = False,
    sep: str = " ",
    end: str = "\n",
) -> None:
    r"""
    scroll gradients on your terminal

    Args:
        *values (Any): *values to print.
        start_color (ColorType): start_color. see examples down below for supported formats.
        end_color (ColorType): end_color. see examples down below for supported formats.
        delay (float, optional): optional, the delay between the change of the gradient, recommended range: .05 - .1
        times (int, optional): optional, the amount of times to change the gradient in place.
        reverse (bool, optional): whether to start with the end color or not.
        sep (:obj:`str`, optional): optional, string inserted between values, default a space.
        end (:obj:`str`, optional): optional, string appended after the last value, default a newline.

    Examples:
        >>> from rgbprint import gradient_scroll, Color
        >>> username = "john doe"
        >>> gradient_scroll("hello", start_color="red", end_color="yellow")
        >>> gradient_scroll("hello", username, "welcome to the app", start_color=Color.forest_green, end_color=0xFF00FF)

        >>> gradient_scroll("[+] loading data, please wait...", start_color="red", end_color="yellow", times=5, delay=.1, end="\r")
        >>> gradient_scroll("[+] loading data, please wait...", start_color="red", end_color="yellow", times=5, delay=.1, reverse=True)

    Raises:
        ValueError: if the color is in an unsupported format, or is out of range of 0-16777215 (0x000000-0xFFFFFF).
        TypeError: if the color is of unsupported type, or the function is missing arguments.
    """

    text = str(sep).join(map(str, values))
    if len(text) % 2:
        text += " "

    start_color = tuple(Color(start_color))
    end_color = tuple(Color(end_color))
    steps = len(text)

    first_half = gradient(start_color, end_color, steps // 2)
    second_half = gradient(end_color, start_color, steps // 2)
    grad = first_half + second_half

    try:
        for _ in range(times * steps):
            grad.append(grad.pop()) if reverse else grad.insert(0, grad.pop())

            for idx, char in enumerate(grad):
                sys.stdout.write(str(Color(char)) + text[idx])
            sys.stdout.write("\r")
            sys.stdout.flush()
            time.sleep(delay)

        sys.stdout.write(end)
    finally:
        sys.stdout.write(Color.reset)
        sys.stdout.flush()
