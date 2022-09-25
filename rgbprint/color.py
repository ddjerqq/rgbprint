from __future__ import annotations

import random
import string
from typing import (
    List,
    Union,
    Tuple,
    Optional,
    Iterable,
    overload,
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    from . import ColorType


def from_str(__color: str) -> Tuple[int, int, int]:
    if __color.startswith("#"):
        __color = __color[1:]
    # try to get the color name
    # maybe it's not malformed, but a color name
    if not all(c in string.hexdigits for c in __color):
        color = getattr(Color, __color, None)
        if color is not None and isinstance(color, Color):
            return tuple(color)
        else:
            raise ValueError("{} is not a valid color string".format(__color))
    # Safety: this will never raise ValueError because we verify the HEX on line 360.
    rgb = tuple(bytes.fromhex(__color))
    if len(rgb) != 3:
        raise ValueError(
            "{} is not a valid color. it must be a hex string in format of RRGGBB or #RRGGBB".format(
                __color
            )
        )
    return rgb


def from_int(__color: int) -> Tuple[int, int, int]:
    b = __color % 256
    g = ((__color - b) // 256) % 256
    r = ((__color - b) // 256 ** 2) - g // 256

    if not all(c in range(0x100) for c in (r, g, b)):
        raise ValueError(
            "color is not proper format. each triplet must be in range 0-255. not {}".format(
                __color
            )
        )

    return r, g, b


def from_iterable(__color: Iterable[int, int, int]) -> Tuple[int, int, int]:
    try:
        r, g, b = list(__color)
    except ValueError as exc:
        raise ValueError(
            "color is in an unsupported format: {}".format(__color)
        ) from exc
    else:
        if not all(c in range(0x100) for c in (r, g, b)):
            raise ValueError(
                "color is in an unsupported format: {}".format(__color)
            )
        return r, g, b


class __InterceptGetattr(type):
    """
    this is a metaclass which will intercept the Class getattr() and convert color tuples into Color objects.
    """

    def __getattribute__(cls, key: str) -> object:
        """
        if we are accessing colors, we want to return color objects, not tuples,
        otherwise we ignore.
        """

        if key == "random":
            # make random act like a property
            return Color(random.randint(0, 16777215))

        attr = object.__getattribute__(cls, key)
        if (
            isinstance(attr, tuple)
            and len(attr) == 3
            and all(isinstance(c, int) for c in attr)
        ):
            return Color(attr)
        else:
            return attr


class Color(metaclass=__InterceptGetattr):
    """
    Color class, to represent a 8bit ANSI color

    instances of this class are printable, meaning when you print it, it changes the color on the terminal.

    all the ways below are valid to initialize a color:

    >>> Color(0xff00ff)
    >>> Color("#ff00ff")
    >>> Color("ff00ff")
    >>> Color([255, 0, 255])
    >>> Color(255, 0, 255)
    >>> Color(255, 0, 0xFF)
    >>> Color.red
    >>> Color.random

    you can also destructure colors like so:
    >>> r, g, b = Color.red
    >>> assert r == 255
    >>> assert g == 0
    >>> assert b == 0
    """

    # region: colors
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    lime = (0, 255, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)
    cyan = (0, 255, 255)
    magenta = (255, 0, 255)
    silver = (192, 192, 192)
    gray = (128, 128, 128)
    maroon = (128, 0, 0)
    olive = (128, 128, 0)
    green = (0, 128, 0)
    purple = (128, 0, 128)
    teal = (0, 128, 128)
    navy = (0, 0, 128)
    dark_red = (139, 0, 0)
    brown = (165, 42, 42)
    firebrick = (178, 34, 34)
    crimson = (220, 20, 60)
    tomato = (255, 99, 71)
    coral = (255, 127, 80)
    indian_red = (205, 92, 92)
    light_coral = (240, 128, 128)
    dark_salmon = (233, 150, 122)
    salmon = (250, 128, 114)
    light_salmon = (255, 160, 122)
    orange_red = (255, 69, 0)
    dark_orange = (255, 140, 0)
    orange = (255, 165, 0)
    gold = (255, 215, 0)
    dark_golden_rod = (184, 134, 11)
    golden_rod = (218, 165, 32)
    pale_golden_rod = (238, 232, 170)
    dark_khaki = (189, 183, 107)
    khaki = (240, 230, 140)
    yellow_green = (154, 205, 50)
    dark_olive_green = (85, 107, 47)
    olive_drab = (107, 142, 35)
    lawn_green = (124, 252, 0)
    chartreuse = (127, 255, 0)
    green_yellow = (173, 255, 47)
    dark_green = (0, 100, 0)
    forest_green = (34, 139, 34)
    lime_green = (50, 205, 50)
    light_green = (144, 238, 144)
    pale_green = (152, 251, 152)
    dark_sea_green = (143, 188, 143)
    medium_spring_green = (0, 250, 154)
    spring_green = (0, 255, 127)
    sea_green = (46, 139, 87)
    medium_aqua_marine = (102, 205, 170)
    medium_sea_green = (60, 179, 113)
    light_sea_green = (32, 178, 170)
    dark_slate_gray = (47, 79, 79)
    dark_cyan = (0, 139, 139)
    aqua = (0, 255, 255)
    light_cyan = (224, 255, 255)
    dark_turquoise = (0, 206, 209)
    turquoise = (64, 224, 208)
    medium_turquoise = (72, 209, 204)
    pale_turquoise = (175, 238, 238)
    aqua_marine = (127, 255, 212)
    powder_blue = (176, 224, 230)
    cadet_blue = (95, 158, 160)
    steel_blue = (70, 130, 180)
    corn_flower_blue = (100, 149, 237)
    deep_sky_blue = (0, 191, 255)
    dodger_blue = (30, 144, 255)
    light_blue = (173, 216, 230)
    sky_blue = (135, 206, 235)
    light_sky_blue = (135, 206, 250)
    midnight_blue = (25, 25, 112)
    dark_blue = (0, 0, 139)
    medium_blue = (0, 0, 205)
    royal_blue = (65, 105, 225)
    blue_violet = (138, 43, 226)
    indigo = (75, 0, 130)
    dark_slate_blue = (72, 61, 139)
    slate_blue = (106, 90, 205)
    medium_slate_blue = (123, 104, 238)
    medium_purple = (147, 112, 219)
    dark_magenta = (139, 0, 139)
    dark_violet = (148, 0, 211)
    dark_orchid = (153, 50, 204)
    medium_orchid = (186, 85, 211)
    thistle = (216, 191, 216)
    plum = (221, 160, 221)
    violet = (238, 130, 238)
    orchid = (218, 112, 214)
    medium_violet_red = (199, 21, 133)
    pale_violet_red = (219, 112, 147)
    deep_pink = (255, 20, 147)
    hot_pink = (255, 105, 180)
    light_pink = (255, 182, 193)
    pink = (255, 192, 203)
    antique_white = (250, 235, 215)
    beige = (245, 245, 220)
    bisque = (255, 228, 196)
    blanched_almond = (255, 235, 205)
    wheat = (245, 222, 179)
    corn_silk = (255, 248, 220)
    lemon_chiffon = (255, 250, 205)
    light_yellow = (255, 255, 224)
    saddle_brown = (139, 69, 19)
    sienna = (160, 82, 45)
    chocolate = (210, 105, 30)
    peru = (205, 133, 63)
    sandy_brown = (244, 164, 96)
    burly_wood = (222, 184, 135)
    tan = (210, 180, 140)
    rosy_brown = (188, 143, 143)
    moccasin = (255, 228, 181)
    navajo_white = (255, 222, 173)
    peach_puff = (255, 218, 185)
    misty_rose = (255, 228, 225)
    lavender_blush = (255, 240, 245)
    linen = (250, 240, 230)
    old_lace = (253, 245, 230)
    papaya_whip = (255, 239, 213)
    sea_shell = (255, 245, 238)
    mint_cream = (245, 255, 250)
    slate_gray = (112, 128, 144)
    light_slate_gray = (119, 136, 153)
    light_steel_blue = (176, 196, 222)
    lavender = (230, 230, 250)
    floral_white = (255, 250, 240)
    alice_blue = (240, 248, 255)
    ghost_white = (248, 248, 255)
    honeydew = (240, 255, 240)
    ivory = (255, 255, 240)
    azure = (240, 255, 255)
    snow = (255, 250, 250)
    dim_gray = (105, 105, 105)
    dark_gray = (169, 169, 169)
    light_gray = (211, 211, 211)
    gainsboro = (220, 220, 220)
    white_smoke = (245, 245, 245)

    random: Color = ...
    reset = "\033[0m"
    # endregion

    __slots__ = ("r", "g", "b")

    # region overloads
    @overload
    def __init__(self, r: int, g: int, b: int) -> None:
        """
        Make a color from red green and blue values passed separately.

        Args:
            r: the value of red as an integer in range 0-255
            g: the value of green as an integer in range 0-255
            b: the value of blue as an integer in range 0-255

        Returns:
            None

        Raises:
             ValueError: if any of the colors passed are in a wrong format. for example out of range of 0-255
        """

    @overload
    def __init__(self, color: str) -> None:
        """
        Make a color from a string.

        Args:
            color: the color's representation in HEX "RRGGBB" or "#RRGGBB" format.

        Returns:
            None

        Notes:
            if you want to use colors by their names do `Color.red` instead.

        Examples:
            >>> good = Color("4BBEE3")
            >>> not_good_but_ok = Color("red")

        Raises:
             ValueError: if the color passed is in a wrong format. for example out of range of 0-255, or the HEX is invalid for example: has more than 6 (RRGGBB) digits.
        """

    @overload
    def __init__(self, color: int) -> None:
        """
        Make a color from an integer.

        Args:
            color: the color's representation as an integer in range 0-16_777_215 (0xFF_FF_FF).

        Returns:
            None

        Examples:
            >>> good = Color(0xFF00FF)
            >>> not_good = Color(0xF4F)
            >>> bad0 = Color(-10)
            >>> bad1 = Color(0xFF00AABB)

        Raises:
             ValueError: if the color passed is in a wrong format. for example out of range of 0x000000-0xFFFFFF
        """

    @overload
    def __init__(self, color: Color) -> None:
        """
        Copy a color from another.

        Args:
            color: the color object

        Returns:
            None

        Examples:
            >>> red0 = Color(255, 0, 0)
            >>> red1 = Color(red0)

        Raises:
             ValueError: if the color passed is in a wrong format. for example out of range of 0x000000-0xFFFFFF
        """

    @overload
    def __init__(self, color: Union[Tuple[int, int, int], List[int, int, int]]) -> None:
        """
        Make a color from an iterable of integers.

        Args:
            color: an iterable yielding the red, green and blue values for the color;

        Returns:
            None

        Examples:
            >>> good = Color((120, 0, 214))
            >>> bad0 = Color([True, "bruh", 123])
            >>> bad1 = Color((-10, 400, 700))

        Raises:
             ValueError: if the color passed is in a wrong format. for example out of range of 0x000000-0xFFFFFF
        """

    # endregion

    def __init__(
        self,
        r: ColorType,
        g: Optional[int] = None,
        b: Optional[int] = None,
    ) -> None:
        if isinstance(r, str):
            # Color("#FF00FF") Color("FF00FF")
            r, g, b = from_str(r)

        elif isinstance(r, Iterable):
            # Color((255, 0, 255))
            r, g, b = from_iterable(r)

        elif isinstance(r, int):

            # Color(255, 0, 255)
            if isinstance(g, int) and isinstance(b, int):
                if not all(c in range(0x100) for c in (r, g, b)):
                    raise ValueError(
                        "color is of unsupported type: {}".format((r, g, b))
                    )

            # Color(0xFF00FF)
            else:
                r, g, b = from_int(r)

        elif isinstance(r, Color):
            r, g, b = r

        else:
            raise TypeError("color is of unsupported type: {}".format((r, g, b)))

        self.r = r
        self.g = g
        self.b = b

    def __iter__(self):
        yield self.r
        yield self.g
        yield self.b

    def __str__(self) -> str:
        return "\033[38;2;{0.r};{0.g};{0.b}m".format(self)

    def __repr__(self) -> str:
        return "Color({0.r}, {0.g}, {0.b})".format(self)

    def __eq__(self, other: Color) -> bool:
        return (
            isinstance(other, Color)
            and self.r == other.r
            and self.g == other.g
            and self.b == other.b
        )
