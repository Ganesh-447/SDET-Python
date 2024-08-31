import pytest
import logging as logger
from ebay.src.utilities.genericUtilites import generate_random_email_and_password


@pytest.mark.tcid_1
def test_create_customer_only_email_password():

    logger.info('create a customer with email and password')

    rand_info = generate_random_email_and_password()
    logger.info(rand_info)
    email = ''
    password = ''

    #create payload
    #make the call
    #verify status code of the call
    # verify email in the response
    # verify customer is created in database