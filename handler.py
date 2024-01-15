from enum import Enum
from pathlib import Path


def checking_file_existence(user_file):
    if Path(user_file).exists():
        return True
    return False


def check_file_extension(user_file, extension):
    if user_file.split('.')[-1] == extension:
        return True
    return False


def read_file(user_file):
    Status = Enum(value='Status', names='SUCCESS FAILURE EMPTY')
    try:
        file = open(user_file, 'r')
        file_data = [row.strip() for row in file]
        if len(file_data) > 0:
            return {'status': Status.SUCCESS.value, 'data': file_data}
        else:
            return {'status': Status.EMPTY.value, 'data': file_data}
    except (NameError, ValueError, OSError):
        return {'status': Status.FAILURE.value, 'data': []}
    finally:
        file.close()


def count_words(data):
    result = dict()
    words = list()
    for piece in data:
        for item in piece.split():
            words.append(item.strip('.,:;?!()'))
    for word in words:
        result[word] = 1 if result.get(word) is None else result[word] + 1
    return dict(sorted(result.items(), key=lambda value: value[1]))
