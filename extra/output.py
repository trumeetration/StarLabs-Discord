from termcolor import cprint
from pyfiglet import figlet_format
from colorama import init
import sys
import os


def show_logo():
    os.system("cls")
    init(strip=not sys.stdout.isatty())
    print("\n")
    logo = figlet_format("STAR LABS", font="banner3")
    cprint(logo, 'light_cyan')
    print("")


def show_dev_info():
    print("\033[36m" + "VERSION: " + "\033[34m" + "1.0" + "\033[34m")
    print("\033[36m"+"DEV: " + "\033[34m" + "https://t.me/StarLabsTech" + "\033[34m")
    print("\033[36m"+"GitHub: " + "\033[34m" + "https://github.com/0xStarLabs/StarLabs-Discord" + "\033[34m")
    print("\033[36m" + "DONATION EVM ADDRESS: " + "\033[34m" + "0x620ea8b01607efdf3c74994391f86523acf6f9e1" + "\033[0m")
    print()


MENU_ITEMS = [
    "Inviter [Token]",
    "Press Button [Token]",
    "Press Reaction [Token]",
    "Change Name [Token]",
    "Change Username [Token + Password]",
    "Change Password [Token + Password]",
    "Change Profile Picture [Token + Password]",
    "Send message to the channel [Token]",
]

CAPTCHA_BOTS = [
    "Nothing",
    "Pandez",
    "CaptchaBot",
    "Sledgehammer",
    "Enter Form"
]
