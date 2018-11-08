import re
import configuration as conf
import pytest

CONF_FILE_PATH = conf.__file__


def helper_get_lineno(to_match, filename):
    to_match = str(to_match)
    with open(filename) as f:
        lineno = 0
        for line in f:
            lineno += 1
            if line.__contains__(to_match):
                return lineno

    f.close()


def test_email_sender_is_string():
    lineno = helper_get_lineno(conf.EMAIL_SENDER, CONF_FILE_PATH)
    assert isinstance(conf.EMAIL_SENDER, str), print(f'Error in {CONF_FILE_PATH}:{lineno}. Expected EMAIL_SENDER to be of type {type("")}, instead it is {type(conf.EMAIL_SENDER)}')


def test_email_has_value():
    lineno = helper_get_lineno(conf.EMAIL_SENDER, CONF_FILE_PATH)
    assert len(conf.EMAIL_SENDER) > 0, print(f"Error in {CONF_FILE_PATH}:{lineno}. EMAIL_SENDER has not been assigned yet.")


def test_email_is_valid(email=None):
    email = conf.EMAIL_SENDER if email is None else email
    pattern = r"[a-z0-9!#$%&'*+\/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+\/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?"
    result = re.search(pattern, email)
    lineno = helper_get_lineno(email, CONF_FILE_PATH)
    assert result is not None, print(f'Error in {CONF_FILE_PATH}:{lineno}. Email: {email} is not a valid email.')
    assert len(result.group()) == len(email), print(f'Email: {email} is not a valid email. Regex matched only a portion of the email. ')


def test_email_list_is_set():
    lineno = helper_get_lineno('EMAIL_RECEIVERS', CONF_FILE_PATH)
    assert len(conf.EMAIL_RECEIVERS) > 0, print(f'{CONF_FILE_PATH}:{lineno}. EMAIL_RECEIVERS list require at least one valid email.')


def test_email_list_has_valid_emails():
    for email in conf.EMAIL_RECEIVERS:
        test_email_is_valid(email)


def run():
    return pytest.main()


if __name__ == '__main__':
    run()
