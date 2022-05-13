from .supported_colors import SupportedColors
from .color import Color

__all__ = ["Fore"]


class Fore:
    RED           = Color(SupportedColors.RED.value)
    LIGHT_RED     = Color(SupportedColors.LIGHT_RED.value)
    DARK_RED      = Color(SupportedColors.DARK_RED.value)
    GREEN         = Color(SupportedColors.GREEN.value)
    LIGHT_GREEN   = Color(SupportedColors.LIGHT_GREEN.value)
    DARK_GREEN    = Color(SupportedColors.DARK_GREEN.value)
    BLUE          = Color(SupportedColors.BLUE.value)
    LIGHT_BLUE    = Color(SupportedColors.LIGHT_BLUE.value)
    DARK_BLUE     = Color(SupportedColors.DARK_BLUE.value)
    YELLOW        = Color(SupportedColors.YELLOW.value)
    LIGHT_YELLOW  = Color(SupportedColors.LIGHT_YELLOW.value)
    CYAN          = Color(SupportedColors.CYAN.value)
    LIGHT_CYAN    = Color(SupportedColors.LIGHT_CYAN.value)
    DARK_CYAN     = Color(SupportedColors.DARK_CYAN.value)
    DARK_YELLOW   = Color(SupportedColors.DARK_YELLOW.value)
    MAGENTA       = Color(SupportedColors.MAGENTA.value)
    LIGHT_MAGENTA = Color(SupportedColors.LIGHT_MAGENTA.value)
    DARK_MAGENTA  = Color(SupportedColors.DARK_MAGENTA.value)
    WHITE         = Color(SupportedColors.WHITE.value)
    GRAY          = Color(SupportedColors.GRAY.value)
    BLACK         = Color(SupportedColors.BLACK.value)
    LIGHT_GRAY    = Color(SupportedColors.LIGHT_GRAY.value)
    DARK_GRAY     = Color(SupportedColors.DARK_GRAY.value)

    RESET         = SupportedColors.RESET.value
