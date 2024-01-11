from menu import *
from colorama import Fore, Back, Style


if __name__ == '__main__':
    intro(Back.CYAN, Fore.MAGENTA, "Word Counter")
    notifier(Fore.MAGENTA, "The program counts how often words appear in a text document.".upper())

