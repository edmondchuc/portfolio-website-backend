"""

Helper functions for tests for the configuration file.

"""


def get_lineno(to_match, filename, search_from=None):
    """
    Get the line number that matches the pattern in a file.

    :param to_match: The pattern to match.
    :type to_match: str
    :param filename: The file name to search.
    :type filename: str
    :param search_from: Search from some position in the file.
    :type search_from: str or None
    :return: The line number found or None if not found.
    :rtype: str or None
    """

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
    """
    Print the error message with the file path and its line number in a nicely formatted string.

    :param filepath: The absolute file path of the file containing the error.
    :type filepath: str
    :param lineno: The line number of the file containing the error.
    :type lineno: int
    :param message: The error message.
    :type message: str
    :return: None
    :rtype: None
    """
    print(f'Error in {filepath}:{lineno}. {message}')


def type_error_message(expected, received):
    """
    Return a nicely formatted string of a type error message.

    :param expected: The type that was expected.
    :type expected: object
    :param received: The variable received.
    :type received: object
    :return: A formatted error message string.
    :rtype: str
    """
    return f'Expected type {expected} but received type {type(received)}.'


if __name__ == '__main__':
    pass