import asyncio

from .fore import Fore
from .gradient import *
from .load_bar import *
from .rgbprint import *


__all__ = ["demo"]

LOGO2 = """
██████╗  ██████╗ ██████╗     ██████╗ ██████╗ ██╗███╗   ██╗████████╗
██╔══██╗██╔════╝ ██╔══██╗    ██╔══██╗██╔══██╗██║████╗  ██║╚══██╔══╝
██████╔╝██║  ███╗██████╔╝    ██████╔╝██████╔╝██║██╔██╗ ██║   ██║   
██╔══██╗██║   ██║██╔══██╗    ██╔═══╝ ██╔══██╗██║██║╚██╗██║   ██║   
██║  ██║╚██████╔╝██████╔╝    ██║     ██║  ██║██║██║ ╚████║   ██║   
╚═╝  ╚═╝ ╚═════╝ ╚═════╝     ╚═╝     ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝   ╚═╝"""


async def _demo():
    s_col = "#EA4DFF"
    e_col = "#99FF33"

    rgbprint("loading rgbprint demo...", color=s_col)
    async for _ in load_bar_async(s_col, e_col, width=100, delay=0.01):
        pass

    gradient_print(LOGO2,
                   start_color=s_col,
                   end_color=e_col,
                   end="")

    gradient_scroll("rgbprint loaded has been loaded!!",
                    start_color=s_col,
                    end_color=e_col,
                    times=3,
                    delay=0.01)

    gradient_change("rgb print is made by @ddjerqq check out the socials, same @ everywhere",
                    start_color=s_col,
                    end_color=e_col,
                    delay=0.03)

    print(f"{Fore.WHITE}[{Fore.LIGHT_CYAN}CRITICAL{Fore.WHITE}] {Fore.CYAN}RGB PRINT 3.0 {Fore.RESET}")
    print(f"{Fore.GRAY}[{Fore.LIGHT_YELLOW}CRITICAL{Fore.GRAY}] {Fore.YELLOW}warning!!{Fore.RESET}")
    print(f"{Fore.DARK_GRAY}[{Fore.LIGHT_RED}CRITICAL{Fore.DARK_GRAY}] {Fore.RED}This is the best library ever! {Fore.RESET}")


def demo():
    asyncio.run(_demo())
