import re
import configuration as conf
import pytest
import tests.helper as help

CONF_FILE_PATH = conf.__file__


def test_email_sender_is_string(email=None):
    lineno = None
    if email is None:
        email = conf.EMAIL_SENDER
        lineno = help.get_lineno('EMAIL_SENDER', CONF_FILE_PATH)
    else:
        lineno = help.get_lineno(email, CONF_FILE_PATH)
    if not isinstance(email, str):
        raise TypeError(help.message(CONF_FILE_PATH, lineno, help.type_error_message(str, type(email))))


def test_email_has_value(email=None):
    email = conf.EMAIL_SENDER if email is None else email
    lineno = help.get_lineno('EMAIL_SENDER', CONF_FILE_PATH)
    assert len(email) is not 0, help.message(CONF_FILE_PATH, lineno, f'EMAIL_SENDER has not been assigned yet.')


def test_email_is_valid(email=None):
    email = conf.EMAIL_SENDER if email is None else email
    pattern = r"[a-z0-9!#$%&'*+\/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+\/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?"
    result = re.search(pattern, email)
    lineno = help.get_lineno(email, CONF_FILE_PATH)
    assert result is not None, print(f'Error in {CONF_FILE_PATH}:{lineno}. Email: {email} is not a valid email.')
    assert len(result.group()) == len(email), print(f'Email: {email} is not a valid email. Regex matched only a portion of the email. ')


def test_email_list_is_set():
    lineno = help.get_lineno('EMAIL_RECEIVERS', CONF_FILE_PATH)
    assert len(conf.EMAIL_RECEIVERS) > 0, print(f'{CONF_FILE_PATH}:{lineno}. EMAIL_RECEIVERS list require at least one valid email.')


def test_email_list_has_valid_emails():
    for email in conf.EMAIL_RECEIVERS:
        test_email_sender_is_string(email)
        test_email_has_value(email)
        test_email_is_valid(email)


def run():
    return pytest.main()


if __name__ == '__main__':
    run()
