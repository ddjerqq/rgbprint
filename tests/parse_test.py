import unittest
import io
import contextlib
from rgbprint import *


class ColorTest(unittest.TestCase):
    def test_parse(self):
        color = Color((255, 0, 0))

        self.assertEqual(color, Color(ColorParser.parse("#FF0000")))
        self.assertEqual(color, Color(ColorParser.parse("FF0000")))
        self.assertEqual(color, Color(ColorParser.parse("red")))
        self.assertEqual(color, Color(ColorParser.parse("RED")))

        with self.assertRaises(ValueError):
            ColorParser.parse("sdbfjshdf")

        self.assertEqual(color, Color(ColorParser.parse(0xFF0000)))
        self.assertEqual(color, Color(ColorParser.parse((255, 0, 0))))


    def test_no_invalid_colors_accepted(self):
        with self.assertRaises(ValueError):
            ColorParser.parse("#FF00FFASD")

        with self.assertRaises(ValueError):
            ColorParser.parse("#FF00FFASD")

        with self.assertRaises(ValueError):
            ColorParser.parse(0xFFF8718723)

        with self.assertRaises(ValueError):
            ColorParser.parse("#FFF8718723")

        with self.assertRaises(ValueError):
            ColorParser.parse((1000, 0, 0))


    def test_rgbprint(self):
        output = io.StringIO()

        with contextlib.redirect_stdout(output):
            rgbprint("hello", color="red")

        self.assertEqual(output.getvalue(), "{}hello\n{}".format(Fore.RED, Fore.RESET))


if __name__ == '__main__':
    unittest.main()
