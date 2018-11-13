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
    """
    Check if the email is a string.

    :param email: The email to be tested.
    :type email: str
    :return: True if the email is a string, else false.
    :rtype: bool
    """
    return isinstance(email, str)


def email_string_is_not_empty(email):
    """
    Check if the string is not empty (i.e. its length is greater than zero).

    :param email: The email to be tested.
    :type email: str
    :return: True if the email is not empty, else false.
    :rtype: bool
    """
    if email_is_string(email):
        return True if len(email) > 0 else False
    return False


def email_is_valid(email):
    """
    Check if the email is a valid email.

    This is done by matching it to a static regular expression pattern.

    :param email: The email to be tested.
    :return: True if the email matches the static regular expression, else false.
    :rtype: bool
    """
    pattern = r"[a-z0-9!#$%&'*+\/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+\/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?"
    return True if re.search(pattern, email) is not None else False


def test_email_sender_is_a_string_and_has_been_set_and_is_valid_email():
    """
    These are not separated into three tests since the last 2 asserts rely on the the email to be a str.

    :return: None
    :rtype: None
    """
    lineno = helper.get_lineno(EMAIL_SENDER, CONF_FILE_PATH)
    assert email_is_string(conf.EMAIL_SENDER), \
        helper.message(
            CONF_FILE_PATH, lineno,
            helper.type_error_message(str, conf.EMAIL_SENDER)
        )
    assert email_string_is_not_empty(conf.EMAIL_SENDER), \
        helper.message(
            CONF_FILE_PATH, lineno, f'{EMAIL_SENDER} string is empty.'
        )
    assert email_is_valid(conf.EMAIL_SENDER), \
        helper.message(
            CONF_FILE_PATH, lineno, f'The {EMAIL_SENDER} has been assigned with an invalid email: {conf.EMAIL_SENDER}'
        )


def test_email_receivers_are_valid():
    """
    These are not separated into three tests since the last 2 asserts rely on the the email to be a str.

    :return: None
    :rtype: None
    """
    for email in conf.EMAIL_RECEIVERS:
        lineno = helper.get_lineno(email, CONF_FILE_PATH, search_from=EMAIL_RECEIVERS)
        assert email_is_string(email), \
            helper.message(CONF_FILE_PATH, lineno, helper.type_error_message(str, email))
        assert email_string_is_not_empty(email), \
            helper.message(CONF_FILE_PATH, helper.get_lineno('\'\'', CONF_FILE_PATH, search_from=EMAIL_RECEIVERS), f'The {EMAIL_RECEIVERS} has an empty string as an email.')
        assert email_is_valid(email), \
            helper.message(CONF_FILE_PATH, lineno, f'{EMAIL_RECEIVERS} has an invalid email: {email}')


def test_website_domain_is_a_string_and_has_been_set():
    lineno = helper.get_lineno(WEBSITE_DOMAIN, CONF_FILE_PATH)
    assert isinstance(conf.WEBSITE_DOMAIN, str), \
        helper.message(CONF_FILE_PATH, lineno, helper.type_error_message(str, conf.WEBSITE_DOMAIN))
    assert len(conf.WEBSITE_DOMAIN) > 0, \
        helper.message(CONF_FILE_PATH, lineno, f'{WEBSITE_DOMAIN} has not been set.')




def run():
    return pytest.main()


if __name__ == '__main__':
    run()
