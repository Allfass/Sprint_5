from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from locators import Locator

class TestLogin():

    def test_login_from_main_page_successful(self, driver, credentials):
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.ENTER_ACCOUNT)))
        element = driver.find_element(By.XPATH, Locator.ENTER_ACCOUNT)
        driver.execute_script("arguments[0].click();", element)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.LOGIN_BUTTON)))
        driver.find_element(By.XPATH, Locator.EMAIL_INPUT).send_keys(credentials['mail'])
        driver.find_element(By.XPATH, Locator.PASS_INPUT).send_keys(credentials['password'])
        driver.find_element(By.XPATH, Locator.LOGIN_BUTTON).click()
        assert driver.find_element(By.XPATH, Locator.CREATE_ORDER_BUTTON) is not None
    
    def test_login_from_account_button_successful(self, driver, credentials):
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.ACCOUNT_BUTTON)))
        element = driver.find_element(By.XPATH, Locator.ACCOUNT_BUTTON)
        driver.execute_script("arguments[0].click();", element)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.LOGIN_BUTTON)))
        driver.find_element(By.XPATH, Locator.EMAIL_INPUT).send_keys(credentials['mail'])
        driver.find_element(By.XPATH, Locator.PASS_INPUT).send_keys(credentials['password'])
        driver.find_element(By.XPATH, Locator.LOGIN_BUTTON).click()
        assert driver.find_element(By.XPATH, Locator.CREATE_ORDER_BUTTON) is not None
    
    def test_login_from_registration_form_successful(self, driver, credentials):
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.ACCOUNT_BUTTON)))
        element = driver.find_element(By.XPATH, Locator.ACCOUNT_BUTTON)
        driver.execute_script("arguments[0].click();", element)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.REGISTRATION_BUTTON)))
        element = driver.find_element(By.XPATH, Locator.REGISTRATION_BUTTON)
        driver.execute_script("arguments[0].click();", element)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.ENTER_ACCOUNT_BUTTON)))
        element = driver.find_element(By.XPATH, Locator.ENTER_ACCOUNT_BUTTON)
        driver.execute_script("arguments[0].click();", element)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.LOGIN_BUTTON)))
        driver.find_element(By.XPATH, Locator.EMAIL_INPUT).send_keys(credentials['mail'])
        driver.find_element(By.XPATH, Locator.PASS_INPUT).send_keys(credentials['password'])
        driver.find_element(By.XPATH, Locator.LOGIN_BUTTON).click()
        assert driver.find_element(By.XPATH, Locator.CREATE_ORDER_BUTTON) is not None
        
    
    def test_login_from_forgot_password_form_successful(self, driver, credentials):
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.ACCOUNT_BUTTON)))
        element = driver.find_element(By.XPATH, Locator.ACCOUNT_BUTTON)
        driver.execute_script("arguments[0].click();", element)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.FORGOT_PASSWORD_BUTTON)))
        element = driver.find_element(By.XPATH, Locator.FORGOT_PASSWORD_BUTTON)
        driver.execute_script("arguments[0].click();", element)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.ENTER_ACCOUNT_BUTTON)))
        element = driver.find_element(By.XPATH, Locator.ENTER_ACCOUNT_BUTTON)
        driver.execute_script("arguments[0].click();", element)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.LOGIN_BUTTON)))
        driver.find_element(By.XPATH, Locator.EMAIL_INPUT).send_keys(credentials['mail'])
        driver.find_element(By.XPATH, Locator.PASS_INPUT).send_keys(credentials['password'])
        driver.find_element(By.XPATH, Locator.LOGIN_BUTTON).click()
        assert driver.find_element(By.XPATH, Locator.CREATE_ORDER_BUTTON) is not None