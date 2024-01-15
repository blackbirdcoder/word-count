from menu import *
from colorama import Fore, Back, Style
from handler import *


if __name__ == '__main__':
    intro(Back.CYAN, Fore.MAGENTA, 'Word Counter')
    notifier(Fore.MAGENTA, 'The program counts how often words appear in a text document.'.upper())
    while True:
        notifier(Fore.YELLOW, 'Enter the path and name of the .txt file')
        filename = receiving_input_data(Fore.YELLOW)
        status = checking_file_existence(filename)
        if not status:
            notifier(Fore.RED, '[!] Please provide the correct path and file name')
        else:
            del status
            status = check_file_extension(filename, 'txt')
            if not status:
                notifier(Fore.RED, '[!] The file extension is not suitable for processing. The file is not .txt')
            else:
                break
    data = read_file(filename)
    if data['status'] == 3:
        notifier(Fore.RED, '[!] File is empty')
    elif data['status'] == 2:
        notifier(Fore.RED, '[!] Unable to open and read file')
    elif data['status'] == 1:
        counted_words = count_words(data['data'])
        show_table(counted_words, ['Word', 'Count'], Fore.MAGENTA, Fore.GREEN)
