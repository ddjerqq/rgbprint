import unittest
from rgbprint import Color


class ColorTest(unittest.TestCase):
    def test_color_creation(self):
        red = Color(255, 0, 0)

        reds = [
            Color(0xff0000),
            Color("#ff0000"),
            Color("ff0000"),
            Color([255, 0, 0]),
            Color(255, 0, 0),
            Color(255, 0, 0),
            Color.red,
        ]

        for color in reds:
            self.assertEqual(color, red)

        color = Color.random


if __name__ == '__main__':
    unittest.main()
