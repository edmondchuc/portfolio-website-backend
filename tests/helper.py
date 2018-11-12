#
# Helper functions for tests
#


def get_lineno(to_match, filename, search_from=None):
    to_match = str(to_match)
    with open(filename) as f:
        lineno = 0
        for line in f:
            lineno += 1
            if search_from:
                if line.__contains__(search_from):
                    search_from = None
            else:
                if line.__contains__(to_match):
                    return lineno
    f.close()


def message(filepath, lineno, message):
    print(f'Error in {filepath}:{lineno}. {message}')


def type_error_message(expected, received):
    return f'Expected type {expected} but received type {type(received)}.'


if __name__ == '__main__':
    pass