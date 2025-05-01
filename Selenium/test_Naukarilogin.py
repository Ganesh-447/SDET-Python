import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

def test_naukari_login():
    driver = webdriver.Chrome()
    driver.get("https://www.naukri.com")
    login = driver.find_element(By.ID, "login_Layer").click()
    time.sleep(1)
    user_name = driver.find_element(By.XPATH, "//input[@placeholder='Enter your active Email ID / Username']")
    password = driver.find_element(By.XPATH, "//input[@placeholder='Enter your password']")
    btn = driver.find_element(By.XPATH, "//button[contains(text(),'Login')]")
    user_name.send_keys("ganeshankarao.grandhi@gmail.com")
    password.send_keys("Anku@123")
    btn.click()
    time.sleep(1)
    three_dots = driver.find_element(By.XPATH, "//div[@class='nI-gNb-bar2']")
    three_dots.click()
    time.sleep(1)
    update_profile = driver.find_element(By.XPATH, "//a[contains(text(),'View')]").click()
    time.sleep(5)
    #driver.maximize_window()
    update_resume = driver.find_element(By.XPATH, "//a[contains(text(),'Update')]")
    update_resume.click()
    #driver.find_element(By.XPATH, "//span[contains(text(),'Add emp')]").click()
    time.sleep(70)


def test_naukari_login_edge():
    driver = webdriver.Edge()
    driver.get("https://www.naukri.com")
    login = driver.find_element(By.ID, "login_Layer").click()
    time.sleep(1)
    user_name = driver.find_element(By.XPATH, "//input[@placeholder='Enter your active Email ID / Username']")
    password = driver.find_element(By.XPATH, "//input[@placeholder='Enter your password']")
    btn = driver.find_element(By.XPATH, "//button[contains(text(),'Login')]")
    user_name.send_keys("grandhiganesh47@gmail.com")
    password.send_keys("Anku@123")
    btn.click()
    time.sleep(1)
    three_dots = driver.find_element(By.XPATH, "//div[@class='nI-gNb-bar2']")
    three_dots.click()
    time.sleep(1)
    update_profile = driver.find_element(By.XPATH, "//a[contains(text(),'View')]").click()
    time.sleep(5)
    # driver.maximize_window()
    update_resume = driver.find_element(By.XPATH, "//a[contains(text(),'Update')]")
    update_resume.click()
    time.sleep(70)

def test_postal_login():
    driver = webdriver.Chrome()
    driver.get("https://dopagent.indiapost.gov.in/corp/AuthenticationController?FORMSGROUP_ID__=AuthenticationFG&__START_TRAN_FLAG__=Y&__FG_BUTTONS__=LOAD&ACTION.LOAD=Y&AuthenticationFG.LOGIN_FLAG=3&BANK_ID=DOP&AGENT_FLAG=Y")
    driver.maximize_window()
    time.sleep(20)
    agent_id = driver.find_element(By.XPATH, "//input[@name ='AuthenticationFG.USER_PRINCIPAL']")
    password = driver.find_element(By.XPATH, "//input[@name ='AuthenticationFG.ACCESS_CODE']")
    log_in = driver.find_element(By.XPATH, "//input[@value ='Log in']")
    agent_id.send_keys("dop.mi5226010400016")
    password.send_keys("kirru@1996")
    log_in.click()
    time.sleep(20)
    accounts = driver.find_element(By.XPATH, "//a[@id='Accounts']")
    accounts.click()
    time.sleep(10)
    books_screen = driver.find_element(By.XPATH, "//a[@id='Agent Enquire & Update Screen']")
    books_screen.click()
    time.sleep(10)
    cash = driver.find_element(By.XPATH,"//input[@id = 'CustomAgentRDAccountFG.PAY_MODE_SELECTED_FOR_TRN' and @value ='C']")
    cash.click()
    account_id = driver.find_element(By.NAME, "CustomAgentRDAccountFG.ACCOUNT_NUMBER_FOR_SEARCH")
    account_id.send_keys("020000056862,020000633166,020005217365,020000668542,020010599107,020016309842,020021973137,"
                         "020057993889,4677849450,4584750887")
    fetch = driver.find_element(By.XPATH,"//input[@name='Action.FETCH_INPUT_ACCOUNT']")
    fetch.click()
    time.sleep(5)
    select_book = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
    for checkbox in select_book:
        checkbox.click()
    save = driver.find_element(By.XPATH,"//input[@name='Action.SAVE_ACCOUNTS']")
    save.click()
    time.sleep(4 * 60 * 60)  # 4 hours,020011116491



