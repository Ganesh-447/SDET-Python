import logging as logger
import random
import string


def generate_random_email_and_password(domain =None, email_prefix=None):
    logger.debug("generating randome email and password.")


    if not domain:

        domain = 'gmail.com'

    if not email_prefix:
        email_prefix = 'testuser'

    random_email_string_length = 10
    random_email_string = ''.join(random.choices(string.ascii_lowercase,k = random_email_string_length))

    email = email_prefix + '_'+random_email_string+'@'+domain

    password_length = 20
    password_string = ''.join(random.choices(string.ascii_letters,k=password_length))

    random_info = {'email':email,'password':password_string}

    return random_info

