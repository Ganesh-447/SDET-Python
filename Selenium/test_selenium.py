from selenium import webdriver
import pytest

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver  # for better memory after returning the driver it's gone.
    # return driver stores the values permanentlty, extra varible

def test_open_url_verify_title(driver):
    driver.get("https://app.vwo.com")
    print(driver.title)
    # verification actual and expected

    assert "Login - VWO" == driver.title

