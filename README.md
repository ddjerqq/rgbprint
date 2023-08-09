# RGBPRINT 4.0.2
![rgbprint-in-rainbow-gradient-color](https://qu.ax/taDN.png)
![rgbprint-blue-purple](https://qu.ax/JLnS.gif)
![rgbprint-blue-purple](https://qu.ax/pKpa.gif)

## Print gradients and colors on your terminal.

## Components:
>
> see below for details.
> 
> - functions
> 
>   - rgbprint
>   - gradient_print
>   - gradient_scroll
>   - gradient_change
>
> - classes
>   - Color

# Basic examples:
> #### use rgbprint:
> ```python
> from rgbprint import rgbprint
> rgbprint("[+] successfully connected to database", color="green")
> ```
> ![rgbprint-green](https://qu.ax/bqVd.png)
> 
> #### inject colors in strings:
> ```python
> from rgbprint import Color
> print(f"[{Color.red}CRITICAL{Color.reset}] encountered error in the program")
> ```
> ![inject-color](https://qu.ax/RQOn.png)
> 
> #### print gradients
> ```python
> from rgbprint import gradient_print, Color
> gradient_print(
>     "[CRITICAL] system failure, program can't open file in location C:/foo/bar/baz.tgz", 
>     start_color=Color.yellow_green, 
>     end_color=Color.dark_magenta
> )
> ```
> ![gradient-print](https://qu.ax/snQA.png)
> 
> #### scroll gradients
> ```python
> from rgbprint import gradient_scroll, Color
> gradient_scroll(
>     "[CRITICAL] system failure, program can't open file in location C:/foo/bar/baz.tgz", 
>     start_color=0x4BBEE3, 
>     end_color=Color.medium_violet_red
> )
> ```
> ![gradient-scroll](https://qu.ax/uyo.gif)
> 
> #### change gradients
> ```python
> from rgbprint import gradient_change, Color
> gradient_change(
>     "[CRITICAL] system failure, program can't open file in location C:/foo/bar/baz.tgz", 
>     start_color=0x4BBEE3, 
>     end_color=Color.medium_violet_red
> )
> ```
> ![gradient-scroll](https://qu.ax/uegj.gif)

# Basic Results
![chimera](https://qu.ax/FMFZ.png)
![ninetails-email-spoofer](https://qu.ax/Cxcj.png)

# Functions:

## rgbprint
![rgbprint-green](https://qu.ax/bqVd.png)
> print but with color keyword argument support.
> 
> Prints the values to sys.stdout.
> 
> the color argument gets converted to a `Color` object before getting printed, thus it must be an instance of `ColorType`
> 
> ```python
> rgbprint(
>       *values, 
>       sep: str = " ",
>       end: str = "\n", 
>       color: Optional[ColorType] = None,
> ) -> None
> ```

> ### Args:
> - *values (`Any`): values to print.
> - color (`ColorType`): `optional` color. see examples down below for supported formats.
> - sep (`str`): `optional`, string inserted between values, default a space.
> - end (`str`): `optional`, string appended after the last value, default a newline.

> ### Examples:
> import the package
> ```python
> from rgbprint import rgbprint 
> from rgbprint import Color 
> ```
> basic colored print
> ```python
> user = "john smith"
> rgbprint("welcome", user, "you are", 25, "years old", color=Color.forest_green)
> ```
> similar functionality to the built-in `print` function, support for unpacking iterables.
> ```python
> rgbprint(*["orange", "apple", "banana"], sep="_", color="yellow")
> ```
> all supported color formats
> ```python
> rgbprint("hello", color="red")
> rgbprint("hello", color=0xff00ff)
> rgbprint("hello", color="#ff00ff")
> rgbprint("hello", color="ff00ff")
> rgbprint("hello", color=[255, 0, 255])
> rgbprint("hello", color=(255, 0, 255))
> rgbprint("hello", color=(255, 0, 0xFF))
> rgbprint("hello", color=Color.red)
> rgbprint("hello", color=Color.random)
> rgbprint("hello", color=Color(255, 0, 127))
> ```

> ### Raises:
> - ValueError: if the color is in an unsupported format, or is out of range of 0-16777215 (0x000000-0xFFFFFF).
> - TypeError: if the color is of unsupported type. or some other error.

## gradient_print
![gradient-print](https://qu.ax/snQA.png)
> print gradients on your terminal
> ```python
> gradient_print(
>       *values, 
>       start_color: Optional[ColorType] = None, 
>       end_color: Optional[ColorType] = None, 
>       sep: str = " ", 
>       end: str = "\n"
> ) -> None
> ```

> ### Args:
> - *values (`Any`): values to print.
> - start_color (`ColorType`): start_color. see examples down below for supported formats.
> - end_color (`ColorType`): end_color. see examples down below for supported formats.
> - sep (`str`): `optional`, string inserted between values, default a space.
> - end (`str`): `optional`, string appended after the last value, default a newline.

> ### Examples:
> import the package
> ```python
> from rgbprint import gradient_print
> from rgbprint import Color 
> ```
> basic gradient scroll
> ```python
> user = "john smith"
> gradient_print("welcome", user, "you are", 25, "years old", start_color="red, end_color="yellow")
> ```
> more examples
> ```python
> username = "john doe"
> gradient_print("hello", start_color="red", end_color="yellow")
> gradient_print("hello", username, "welcome to the app", start_color=Color.forest_green, end_color=0xFF00FF)
> gradient_print("[+] loading data, please wait...", start_color=Color.aqua_marine, end_color=Color.peach_puff)
> ```
> similar functionality to the built-in `print` function, support for unpacking iterables.
> ```python
> gradient_print(*["orange", "apple", "banana"], sep="_", start_color="yellow", end_color="red")
> ```
> all supported color formats
> ```python
> gradient_print("hello", start_color="red",              end_color="red")
> gradient_print("hello", start_color=0xff00ff,           end_color=0xff00ff)
> gradient_print("hello", start_color="#ff00ff",          end_color="#ff00ff")
> gradient_print("hello", start_color="ff00ff",           end_color="ff00ff")
> gradient_print("hello", start_color=[255, 0, 255],      end_color=[255, 0, 255])
> gradient_print("hello", start_color=(255, 0, 255),      end_color=(255, 0, 255))
> gradient_print("hello", start_color=(255, 0, 0xFF),     end_color=(255, 0, 0xFF))
> gradient_print("hello", start_color=Color.red,          end_color=Color.red)
> gradient_print("hello", start_color=Color.random,       end_color=Color.random)
> gradient_print("hello", start_color=Color(255, 0, 127), end_color=Color(255, 0, 127))
> ```

> ### Raises:
> - ValueError: if the color is in an unsupported format, or is out of range of 0-16777215 (0x000000-0xFFFFFF).
> - TypeError: if the color is of unsupported type, or the function is missing arguments.

## gradient_scroll
![gradient-scroll](https://qu.ax/uyo.gif)
> scroll gradients on your terminal
> ```python
> gradient_scroll(
>       *values, 
>       start_color: Optional[ColorType] = None, 
>       end_color: Optional[ColorType] = None,
>       delay: float = 0.03,
>       times: int = 4,
>       reverse: bool = False,
>       sep: str = " ", 
>       end: str = "\n",
> ) -> None
> ```

> ### Args:
> - *values (`Any`): values to print.
> - start_color (`ColorType`): start_color. see examples down below for supported formats.
> - end_color (`ColorType`): end_color. see examples down below for supported formats.
> - delay (`float`): `optional`, the delay between the change of the gradient, recommended range: .05 - .1
> - times (`int`): `optional`, the amount of times to change the gradient in place.
> - reverse (`bool`): `optional` whether to start with the end color or not.
> - sep (`str`): `optional`, string inserted between values, default a space.
> - end (`str`): `optional`, string appended after the last value, default a newline.

> ### Examples:
> import the package
> ```python
> from rgbprint import gradient_scroll
> from rgbprint import Color 
> ```
> basic gradient print
> ```python
> user = "john smith"
> gradient_scroll("welcome", user, "you are", 25, "years old", start_color="red", end_color="yellow")
> ```
> more examples
> ```python
> username = "john doe"
> gradient_scroll("hello", start_color="red", end_color="yellow")
> gradient_scroll("hello", start_color="red", end_color="yellow", delay=0.1)
> gradient_scroll("hello", start_color="red", end_color="yellow", delay=0.1, times=10)
> gradient_scroll("hello", start_color="red", end_color="yellow", delay=0.1, times=10, reverse=True)
> gradient_scroll("hello", username, "welcome to the app", start_color=Color.forest_green, end_color=0xFF00FF)
> gradient_scroll("[+] loading data, please wait...", start_color=Color.aqua_marine, end_color=Color.peach_puff)
> ```
> similar functionality to the built-in `print` function, support for unpacking iterables.
> ```python
> gradient_scroll(*["orange", "apple", "banana"], sep="_", start_color="yellow", end_color="red")
> ```
> all supported color formats
> ```python
> gradient_scroll("hello", start_color="red",              end_color="red")
> gradient_scroll("hello", start_color=0xff00ff,           end_color=0xff00ff)
> gradient_scroll("hello", start_color="#ff00ff",          end_color="#ff00ff")
> gradient_scroll("hello", start_color="ff00ff",           end_color="ff00ff")
> gradient_scroll("hello", start_color=[255, 0, 255],      end_color=[255, 0, 255])
> gradient_scroll("hello", start_color=(255, 0, 255),      end_color=(255, 0, 255))
> gradient_scroll("hello", start_color=(255, 0, 0xFF),     end_color=(255, 0, 0xFF))
> gradient_scroll("hello", start_color=Color.red,          end_color=Color.red)
> gradient_scroll("hello", start_color=Color.random,       end_color=Color.random)
> gradient_scroll("hello", start_color=Color(255, 0, 127), end_color=Color(255, 0, 127))
> ```

> ### Raises:
> - ValueError: if the color is in an unsupported format, or is out of range of 0-16777215 (0x000000-0xFFFFFF).
> - TypeError: if the color is of unsupported type, or the function is missing arguments.

## gradient_change
![gradient-scroll](https://qu.ax/uegj.gif)
> change gradients in place on your terminal
> this function is very similar to `gradient_scroll` almost identical.
> ```python
> gradient_change(
>       *values, 
>       start_color: Optional[ColorType] = None, 
>       end_color: Optional[ColorType] = None,
>       delay: float = 0.03,
>       times: int = 4,
>       reverse: bool = False,
>       sep: str = " ", 
>       end: str = "\n",
> ) -> None
> ```

> ### Args:
> - *values (`Any`): values to print.
> - start_color (`ColorType`): start_color. see examples down below for supported formats.
> - end_color (`ColorType`): end_color. see examples down below for supported formats.
> - delay (`float`): `optional`, the delay between the change of the gradient, recommended range: .05 - .1
> - times (`int`): `optional`, the amount of times to change the gradient in place.
> - reverse (`bool`): `optional` whether to start with the end color or not.
> - sep (`str`): `optional`, string inserted between values, default a space.
> - end (`str`): `optional`, string appended after the last value, default a newline.

> ### Examples:
> import the package
> ```python
> from rgbprint import gradient_change
> from rgbprint import Color 
> ```
> basic gradient print
> ```python
> user = "john smith"
> gradient_change("welcome", user, "you are", 25, "years old", start_color="red, end_color="yellow")
> ```
> more examples
> ```python
> username = "john doe"
> gradient_change("hello", start_color="red", end_color="yellow")
> gradient_change("hello", start_color="red", end_color="yellow", delay=0.1)
> gradient_change("hello", start_color="red", end_color="yellow", delay=0.1, times=10)
> gradient_change("hello", start_color="red", end_color="yellow", delay=0.1, times=10, reverse=True)
> gradient_change("hello", username, "welcome to the app", start_color=Color.forest_green, end_color=0xFF00FF)
> gradient_change("[+] loading data, please wait...", start_color=Color.aqua_marine, end_color=Color.peach_puff)
> ```
> similar functionality to the built-in `print` function, support for unpacking iterables.
> ```python
> gradient_change(*["orange", "apple", "banana"], sep="_", start_color="yellow", end_color="red")
> ```
> all supported color formats
> ```python
> gradient_change("hello", start_color="red",              end_color="red")
> gradient_change("hello", start_color=0xff00ff,           end_color=0xff00ff)
> gradient_change("hello", start_color="#ff00ff",          end_color="#ff00ff")
> gradient_change("hello", start_color="ff00ff",           end_color="ff00ff")
> gradient_change("hello", start_color=[255, 0, 255],      end_color=[255, 0, 255])
> gradient_change("hello", start_color=(255, 0, 255),      end_color=(255, 0, 255))
> gradient_change("hello", start_color=(255, 0, 0xFF),     end_color=(255, 0, 0xFF))
> gradient_change("hello", start_color=Color.red,          end_color=Color.red)
> gradient_change("hello", start_color=Color.random,       end_color=Color.random)
> gradient_change("hello", start_color=Color(255, 0, 127), end_color=Color(255, 0, 127))
> ```

> ### Raises:
> - ValueError: if the color is in an unsupported format, or is out of range of 0-16777215 (0x000000-0xFFFFFF).
> - TypeError: if the color is of unsupported type, or the function is missing arguments.

# Classes:

## Color
> Color class, to represent a 8bit ANSI colors
> 
> instances of this class are printable, when you print them, they change the color of your terminal.
> ```python
> Color(r, g, b)
> ```

> ## Slots:
> 
> - r: (`int` in `0..256`): red value of the color
> - g: (`int` in `0..256`): green value of the color
> - b: (`int` in `0..256`): blue value of the color

> ## Initialization: 
> all the ways below are valid to initialize a color:
> ```python
> Color(0xff00ff)
> Color("#ff00ff")
> Color("ff00ff")
> Color([255, 0, 255])
> Color(255, 0, 255)
> Color(255, 0, 0xFF)
> Color(Color.red)
> Color(Color.random)
> ```

> ## Different ways to initialize colors: 
> colors can be initialized in many ways:
> - `Color(int, int, int)` 
>   - `Color(255, 0, 255)` 
>   - `Color(0x4B, 0xBB, 0xE3)` 
>   - `Color(*(127, 127, 127))` 
>
> 
> - `Color(str)`
>   - `Color("#FF00FF")` 
>   - `Color("FF00FF")` 
>   - `Color("red)` 
>   - `Color("green")`
>
> 
> - `Color(int)`
>   - `Color(0x4BBEE3)` 
>   - `Color(16777215)`
> 
> 
> - `Color(Color)`
>   - `red = Color.red; Color(red)`
> 
> 
> - `Color(Tuple[int, int, int] | List[int, int, int])`
>   - `Color((100, 255, 16))`
>   - `Color([100, 255, 16])`
 
> ## Destruction
> you can destruct colors into its red, green, blue components like so:
> ```python
> r, g, b = Color.red
> assert r == 255
> assert g == 0
> assert b == 0
> 
> rgb = tuple(Color("FF00FF"))
> assert isinstance(rgb, tuple)
> assert rgb == (255, 0, 255)
> ```

> ## Dunder/magic method implementations:
> the color class has some dunder magic methods implemented.
> 
> - `__iter__` to destruct the colors.
> - `__str__` to print the colors
> - `__repr__` to represent colors for debugging purposes.
> - `__eq__` to compare 2 colors, and see if they are the same color.
