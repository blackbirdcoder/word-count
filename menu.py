from colorama import Style
from prettytable import PrettyTable
from tqdm import tqdm


def intro(bg_color, color, title):
    MULTI = 25
    print(bg_color + color + "#" * MULTI + f" {title} ".upper() + "#" * MULTI + Style.RESET_ALL)


def notifier(color, text):
    print(color + text + Style.RESET_ALL)


def receiving_input_data(color):
    marker = color + ">" + Style.RESET_ALL
    return input(marker)


def show_table(data_words, fields_names, color_bar, color_table):
    table = PrettyTable()
    table.field_names = [fields_names[0], fields_names[1]]
    for item in tqdm(data_words.items(), ascii=True, desc=color_bar + 'Process'):
        table.add_row([item[0], item[1]])
    print(color_table)
    print(table)
    print(Style.RESET_ALL)
