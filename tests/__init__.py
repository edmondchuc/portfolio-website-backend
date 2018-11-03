import re

import configuration as conf


def test_email_sender_is_string():
    if isinstance(conf.EMAIL_SENDER, str):
        pass
    else:
        raise Exception(f'EMAIL_SENDER must be of type string but found {type(conf.EMAIL_SENDER)}')


def test_email_has_value():
    if len(conf.EMAIL_SENDER) is 0:
        raise Exception('EMAIL_SENDER has not been assigned yet.')


def test_email_is_valid(email=None):
    email = conf.EMAIL_SENDER if email is None else email
    pattern = "[a-z0-9!#$%&'*+\/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+\/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?"
    result = re.search(pattern, email)
    if result is None:
        raise Exception(f'Email:{email} is not a valid email.')
    if len(result.group()) is not len(email):
        raise Exception(f'Email:{email} is not a valid email. Regex matched only a portion of the email.')


def test_email_list_is_set():
    if len(conf.EMAIL_RECEIVERS) is 0:
        raise Exception('EMAIL_RECEIVERS list require at least one valid email.')


def test_email_list_has_valid_emails():
    for email in conf.EMAIL_RECEIVERS:
        test_email_is_valid(email)


def run():
    test_email_sender_is_string()
    test_email_has_value()
    test_email_is_valid()
    test_email_list_is_set()
    test_email_list_has_valid_emails()
    print('All tests passed.')

if __name__ == '__main__':
    run()