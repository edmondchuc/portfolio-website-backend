import re
import configuration as conf
import pytest
import tests.helper as helper

CONF_FILE_PATH = conf.__file__

# constant variables being tested against (used to reduce human error)
EMAIL_SENDER = 'EMAIL_SENDER'
EMAIL_RECEIVERS = 'EMAIL_RECEIVERS'
WEBSITE_DOMAIN = 'WEBSITE_DOMAIN'


def email_is_string(email):
    return isinstance(email, str)


def email_string_is_not_empty(email):
    if email_is_string(email):
        return True if len(email) > 0 else False
    return False


def email_is_valid(email):
    pattern = r"[a-z0-9!#$%&'*+\/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+\/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?"
    return True if re.search(pattern, email) is not None else False


def test_email_sender_is_string():
    lineno = helper.get_lineno(EMAIL_SENDER, CONF_FILE_PATH)
    assert email_is_string(conf.EMAIL_SENDER), \
    helper.message(
        CONF_FILE_PATH, lineno,
        helper.type_error_message(str, conf.EMAIL_SENDER)
    )


def test_email_sender_string_is_not_empty():
    lineno = helper.get_lineno(EMAIL_SENDER, CONF_FILE_PATH)
    assert email_string_is_not_empty(conf.EMAIL_SENDER), \
    helper.message(
        CONF_FILE_PATH, lineno, f'{EMAIL_SENDER} string is empty.'
    )


def test_email_of_sender_is_valid():
    lineno = helper.get_lineno(EMAIL_SENDER, CONF_FILE_PATH)
    assert email_is_valid(conf.EMAIL_SENDER), \
    helper.message(
        CONF_FILE_PATH, lineno, f'The {EMAIL_SENDER} has been assigned with an invalid email: {conf.EMAIL_SENDER}'
    )


def test_email_receivers_are_valid():
    for email in conf.EMAIL_RECEIVERS:
        lineno = helper.get_lineno(email, CONF_FILE_PATH, search_from=EMAIL_RECEIVERS)
        result = email_is_string(email)
        assert result, \
        helper.message(CONF_FILE_PATH, lineno, helper.type_error_message(str, email))
        if result:
            assert email_string_is_not_empty(email), \
            helper.message(CONF_FILE_PATH, lineno, f'The {EMAIL_RECEIVERS} has an empty string as an email.')
            assert email_is_valid(email), \
            helper.message(CONF_FILE_PATH, lineno, f'{EMAIL_RECEIVERS} has an invalid email: {email}')


def test_website_domain_is_a_string():
    lineno = helper.get_lineno(WEBSITE_DOMAIN, CONF_FILE_PATH)
    assert isinstance(conf.WEBSITE_DOMAIN, str), \
    helper.message(CONF_FILE_PATH, lineno, helper.type_error_message(str, conf.WEBSITE_DOMAIN))


def test_website_domain_is_set():
    lineno = helper.get_lineno(WEBSITE_DOMAIN, CONF_FILE_PATH)
    assert len(conf.WEBSITE_DOMAIN) > 0, \
    helper.message(CONF_FILE_PATH, lineno, f'{WEBSITE_DOMAIN} has not been set.')




def run():
    return pytest.main()


if __name__ == '__main__':
    run()
#TODO: make the tests on strings and type to be independent. The test that checks the length will result in type error if it's not a string.