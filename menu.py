from colorama import Style


def intro(bg_color, color, title):
    MULTI = 25
    print(bg_color + color + "#" * MULTI + f" {title} ".upper() + "#" * MULTI + Style.RESET_ALL)


def notifier(color, text):
    print(color + text + Style.RESET_ALL)


def receiving_input_data(color):
    marker = color + ">" + Style.RESET_ALL
    return input(marker)
