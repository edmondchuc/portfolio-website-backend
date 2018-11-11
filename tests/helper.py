def get_lineno(to_match, filename):
    to_match = str(to_match)
    with open(filename) as f:
        lineno = 0
        for line in f:
            lineno += 1
            if line.__contains__(to_match):
                return lineno

    f.close()


def message(filepath, lineno, message):
    print(f'Error in {filepath}:{lineno}. {message}')
    return message


def type_error_message(expected, received):
    return f'Expected type {expected} but received type {received}.'


if __name__ == '__main__':
    pass