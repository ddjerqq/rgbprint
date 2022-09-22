import io
import unittest
import contextlib

from rgbprint import *


class GenericTest(unittest.TestCase):
    def test_fore(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            rgbprint("TEST", __color=Color.red)
        self.assertEqual(out.getvalue(), "\033[38;2;255;0;0mTEST\n\033[0m")

    def test_color(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            rgbprint("TEST", __color=Color("#FF0000"))
        self.assertEqual(out.getvalue(), "\033[38;2;255;0;0mTEST\n\033[0m")

    def test_rgbprint(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            rgbprint("TEST", __color=(255, 0, 0))
        self.assertEqual(out.getvalue(), "\033[38;2;255;0;0mTEST\n\033[0m")

    def test_color_get_attr(self):
        print(f"{Color.red}hi{Color.reset}")


if __name__ == '__main__':
    unittest.main()
