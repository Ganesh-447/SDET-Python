import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

def test_naukari_login():
    driver = webdriver.Edge()
    driver.get("")
    time.sleep(50)