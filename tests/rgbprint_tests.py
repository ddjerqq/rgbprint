import io
import unittest
import contextlib

from rgbprint import *


class ColorTest(unittest.TestCase):
    color_names = (
        "black",
        "white",
        "red",
        "lime",
        "blue",
        "yellow",
        "cyan",
        "magenta",
        "silver",
        "gray",
        "maroon",
        "olive",
        "green",
        "purple",
        "teal",
        "navy",
        "dark_red",
        "brown",
        "firebrick",
        "crimson",
        "tomato",
        "coral",
        "indian_red",
        "light_coral",
        "dark_salmon",
        "salmon",
        "light_salmon",
        "orange_red",
        "dark_orange",
        "orange",
        "gold",
        "dark_golden_rod",
        "golden_rod",
        "pale_golden_rod",
        "dark_khaki",
        "khaki",
        "yellow_green",
        "dark_olive_green",
        "olive_drab",
        "lawn_green",
        "chartreuse",
        "green_yellow",
        "dark_green",
        "forest_green",
        "lime_green",
        "light_green",
        "pale_green",
        "dark_sea_green",
        "medium_spring_green",
        "spring_green",
        "sea_green",
        "medium_aqua_marine",
        "medium_sea_green",
        "light_sea_green",
        "dark_slate_gray",
        "dark_cyan",
        "aqua",
        "light_cyan",
        "dark_turquoise",
        "turquoise",
        "medium_turquoise",
        "pale_turquoise",
        "aqua_marine",
        "powder_blue",
        "cadet_blue",
        "steel_blue",
        "corn_flower_blue",
        "deep_sky_blue",
        "dodger_blue",
        "light_blue",
        "sky_blue",
        "light_sky_blue",
        "midnight_blue",
        "dark_blue",
        "medium_blue",
        "royal_blue",
        "blue_violet",
        "indigo",
        "dark_slate_blue",
        "slate_blue",
        "medium_slate_blue",
        "medium_purple",
        "dark_magenta",
        "dark_violet",
        "dark_orchid",
        "medium_orchid",
        "thistle",
        "plum",
        "violet",
        "orchid",
        "medium_violet_red",
        "pale_violet_red",
        "deep_pink",
        "hot_pink",
        "light_pink",
        "pink",
        "antique_white",
        "beige",
        "bisque",
        "blanched_almond",
        "wheat",
        "corn_silk",
        "lemon_chiffon",
        "light_yellow",
        "saddle_brown",
        "sienna",
        "chocolate",
        "peru",
        "sandy_brown",
        "burly_wood",
        "tan",
        "rosy_brown",
        "moccasin",
        "navajo_white",
        "peach_puff",
        "misty_rose",
        "lavender_blush",
        "linen",
        "old_lace",
        "papaya_whip",
        "sea_shell",
        "mint_cream",
        "slate_gray",
        "light_slate_gray",
        "light_steel_blue",
        "lavender",
        "floral_white",
        "alice_blue",
        "ghost_white",
        "honeydew",
        "ivory",
        "azure",
        "snow",
        "dim_gray",
        "dark_gray",
        "light_gray",
        "gainsboro",
        "white_smoke",
    )

    def test_color_creation(self):
        red = Color(255, 0, 0)

        reds = [
            Color(0xFF0000),
            Color("#ff0000"),
            Color("ff0000"),
            Color([255, 0, 0]),
            Color((255, 0, 0)),
            Color(255, 0, 0),
            Color(0xff, 0, 0),
            Color.red,
        ]

        for color in reds:
            self.assertEqual(color, red)

    def test_get_named_color(self):
        for color_name in self.color_names:
            getattr(Color, color_name)

    def test_color_copy(self):
        red0 = Color.red
        red1 = Color(red0)

        self.assertEqual(red0, red1)

    def test_random_color(self):
        rand = Color.random

    def test_bad_color_values(self):
        self.assertRaises(ValueError, lambda: Color(0xFF0000FF))
        self.assertRaises(ValueError, lambda: Color("foo"))
        self.assertRaises(ValueError, lambda: Color("#ff0000FF"))
        self.assertRaises(ValueError, lambda: Color("ff0000FF"))
        self.assertRaises(ValueError, lambda: Color([255, 0, 0, 255]))
        self.assertRaises(ValueError, lambda: Color([255, 0, -100, 255]))
        self.assertRaises(ValueError, lambda: Color((255, 0, 0, 700)))
        self.assertRaises(ValueError, lambda: Color(255, 0, -100))
        self.assertRaises(ValueError, lambda: Color(0xff, 0, 700))
        self.assertRaises(ValueError, lambda: Color("bruh"))
        self.assertRaises(ValueError, lambda: Color(b"bytes?"))

    def test_bad_color_types(self):
        self.assertRaises(TypeError, lambda: Color(None))  # type: ignore
        self.assertRaises(TypeError, lambda: Color(type))  # type: ignore
        self.assertRaises(TypeError, lambda: Color(int))   # type: ignore

    def test_repr_of_color(self):
        red = Color.red
        self.assertEqual(repr(red), "Color(255, 0, 0)")


class GradientTest(unittest.TestCase):
    def test_gradient_print(self):
        gradient_print("TEST", start_color="red", end_color=0)
        gradient_print("TEST", start_color=Color.random, end_color=Color.random)

    def test_gradient_scroll(self):
        gradient_scroll("TEST", start_color="red", end_color=0)
        gradient_scroll("TEST", start_color="red", end_color=0, times=1)
        gradient_scroll("TEST", start_color="red", end_color=0, times=1, delay=.1)
        gradient_scroll("TEST", start_color="red", end_color=0, times=1, delay=.1, reverse=True)

    def test_gradient_change(self):
        gradient_change("TEST", start_color="red", end_color=0)
        gradient_change("TEST", start_color="red", end_color=0, times=1)
        gradient_change("TEST", start_color="red", end_color=0, times=1, delay=.1)
        gradient_change("TEST", start_color="red", end_color=0, times=1, delay=.1, reverse=True)

    def test_odd_chars_in_gradient(self):
        gradient_print("TESTERS", start_color="red", end_color=0)
        gradient_scroll("TESTERS", start_color="red", end_color=0)
        gradient_change("TESTERS", start_color="red", end_color=0)


class GenericTest(unittest.TestCase):
    def test_named_color_attribute(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            rgbprint("TEST", color=Color.red)
        self.assertEqual(out.getvalue(), "\033[38;2;255;0;0mTEST\n\033[0m")

    def test_str_color(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            rgbprint("TEST", color=Color("#FF0000"))
        self.assertEqual(out.getvalue(), "\033[38;2;255;0;0mTEST\n\033[0m")

    def test_args_color(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            rgbprint("TEST", color=Color(255, 0, 0))
        self.assertEqual(out.getvalue(), "\033[38;2;255;0;0mTEST\n\033[0m")

    def test_random_color_correct_str(self):
        for _ in range(100):
            color = Color.random
            r, g, b = color
            self.assertEqual(str(color), f"\033[38;2;{r};{g};{b}m")

    def test_color_copying(self):
        red0 = Color.red
        red1 = Color(red0)
        self.assertEqual(tuple(red0), tuple(red1))


if __name__ == "__main__":
    unittest.main()
