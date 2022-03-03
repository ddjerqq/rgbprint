import random


class Colors:
    """
    The struct for default colors. \n
    >>> Colors.RED
    >>> Colors.BLUE
    >>> Colors.random()
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
    LIGHT_GRAY = (192, 192, 192)
    GRAY = (128, 128, 128)
    DARK_GRAY = (64, 64, 64)
    BLACK = (0, 0, 0)




