import pytest
import logging as logger



@pytest.mark.tcid_1
def test_create_customer_only_email_password():

    logger.info('create a customer with email and password')
    email = ''
    password = ''

    #create payload
    #make the call
    #verify status code of the call
    # verify email in the response
    # verify customer is created in database