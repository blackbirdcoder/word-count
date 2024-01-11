from pathlib import Path


def checking_file_existence(user_file):
    if Path(user_file).exists():
        return True
    return False


def check_file_extension(user_file, extension):
    if user_file.split('.')[-1] == extension:
        return True
    return False


