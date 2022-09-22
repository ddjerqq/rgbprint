import sys
import time
from typing import Tuple, List, Any, Union

from .color import Color

__all__ = ["gradient", "gradient_print", "gradient_change", "gradient_scroll"]


def gradient(start: Tuple[int, int, int], end: Tuple[int, int, int], steps: int) -> List[Tuple[int, int, int]]:
    """
    generate gradients with start color, end color and amount of steps.
    -------------------------------------------------------------------
    :param start: start color, this must be a tuple of 3 ints.
    :param end: end color, this must be a tuple of 3 ints.
    :param steps: amount of steps.
    """
    rs = [start[0]]
    gs = [start[1]]
    bs = [start[2]]
    for step in range(1, steps):
        rs.append(round(start[0] + (end[0] - start[0]) * step / steps))
        gs.append(round(start[1] + (end[1] - start[1]) * step / steps))
        bs.append(round(start[2] + (end[2] - start[2]) * step / steps))

    return list(zip(rs, gs, bs))


def gradient_print(
        *values: Any,
        start_color: Union[str, int, Tuple[int, int, int], Color],
        end_color: Union[str, int, Tuple[int, int, int], Color],
        sep: str = " ",
        end: str = "\n") -> None:
    """
    print gradients.
    ----------------
    note:
        you must pass both `start_color` and `end_color`.
    raises:
        ValueError: if start_color and end_color are invalid, or unsupported format.

    :param values: any value, will be auto-cast to str.
    :param start_color: start color, this can be in any supported format.
    :param end_color: end color, this can be in any supported format.
    :param sep: separator, gets auto-cast to str.
    :param end: end char, gets auto-cast to str.
    """

    text = str(sep).join(map(str, values))

    start_color = ColorParser.parse(start_color)
    end_color = ColorParser.parse(end_color)

    steps = len(text)

    grad = gradient(start_color, end_color, steps)

    try:
        for i, char in enumerate(text):
            color = grad[i]
            sys.stdout.write(str(Color(color)) + char)
        sys.stdout.write(str(end))
    finally:
        sys.stdout.write(Fore.RESET)
        sys.stdout.flush()


def gradient_change(
        *values: Any,
        start_color: Union[str, int, Tuple[int, int, int], Color],
        end_color: Union[str, int, Tuple[int, int, int], Color],
        delay: float = 0.05,
        sep: str = " ",
        end: str = "\n") -> None:
    """
    print gradients and change in place from start_color to end_color in same place. \n
    note:
        both start_color and end_color must be passed.
        THIS DOES NOT WORK WITH MULTILINE TEXTS `YET`. \n
    raises:
        ValueError: if start_color and end_color are invalid, or unsupported format.
    --------------------------------------------------------------------------------
    :param values: any value, will be auto-cast to str.
    :param start_color: start color, this can be in any supported format.
    :param end_color: end color, this can be in any supported format.
    :param delay: delay between each change, recommended to be between 0.005 and 0.1.
    :param sep: separator, gets auto-cast to str.
    :param end: end char, gets auto-cast to str.
    """

    text = str(sep).join(map(str, values))

    start_color = ColorParser.parse(start_color)
    end_color = ColorParser.parse(end_color)
    steps = len(text)
    grad = gradient(start_color, end_color, steps)

    try:
        for idx in range(steps):
            sys.stdout.write(str(Color(grad[idx])) + "\r" + text)
            sys.stdout.flush()
            time.sleep(delay)
        sys.stdout.write(end)
    finally:
        sys.stdout.write(Fore.RESET)
        sys.stdout.flush()


def gradient_scroll(
        *values: Any,
        start_color: Union[str, int, Tuple[int, int, int], Color],
        end_color: Union[str, int, Tuple[int, int, int], Color],
        delay: float = 0.03,
        times: int = 4,
        reverse: bool = False,
        sep: str = " ",
        end: str = "\n") -> None:
    """
    scroll gradient text horizontally \n
    note:
        both start_color and end_color must be passed. \n
        THIS DOES NOT WORK WITH MULTILINE TEXTS `YET`.  \n
    raises:
        ValueError: if start_color and end_color are invalid, or unsupported format.
    --------------------
    :param values: any value, will be auto-cast to str.
    :param start_color: start color, this can be in any supported format.
    :param end_color: end color, this can be in any supported format.
    :param delay: delay between each change, recommended to be lower than 0.1
    :param times: number of times to scroll
    :param reverse: reverse the gradient
    :param sep: separator, gets auto-cast to str
    :param end: end char, gets auto-cast to str
    """
    text = str(sep).join(map(str, values))
    if len(text) % 2:
        text += " "

    start_color = ColorParser.parse(start_color)
    end_color = ColorParser.parse(end_color)
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
        sys.stdout.write(Fore.RESET)
        sys.stdout.flush()
