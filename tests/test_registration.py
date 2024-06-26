from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from locators import Locator

class TestRegistration():

    def test_valid_mail_and_password_get_successful_registration(self, driver, random_credentials):
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.ACCOUNT_BUTTON)))
        element = driver.find_element(By.XPATH, Locator.ACCOUNT_BUTTON)
        driver.execute_script("arguments[0].click();", element)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.REGISTRATION_BUTTON)))
        element = driver.find_element(By.XPATH, Locator.REGISTRATION_BUTTON)
        driver.execute_script("arguments[0].click();", element)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.NAME_INPUT)))
        driver.find_element(By.XPATH, Locator.NAME_INPUT).send_keys(random_credentials['user'])
        driver.find_element(By.XPATH, Locator.EMAIL_INPUT).send_keys(random_credentials['mail'])
        driver.find_element(By.XPATH, Locator.PASS_INPUT).send_keys(random_credentials['password'])
        driver.find_element(By.XPATH, Locator.REGISTRATION_COMMIT_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.LOGIN_BUTTON)))
        driver.find_element(By.XPATH, Locator.EMAIL_INPUT).send_keys(random_credentials['mail'])
        driver.find_element(By.XPATH, Locator.PASS_INPUT).send_keys(random_credentials['password'])
        driver.find_element(By.XPATH, Locator.LOGIN_BUTTON).click()
        assert driver.find_element(By.XPATH, Locator.CREATE_ORDER_BUTTON) is not None
        
    def test_valid_mail_and_invalid_password_return_error(self, driver, random_credentials):
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.ACCOUNT_BUTTON)))
        element = driver.find_element(By.XPATH, Locator.ACCOUNT_BUTTON)
        driver.execute_script("arguments[0].click();", element)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.REGISTRATION_BUTTON)))
        element = driver.find_element(By.XPATH, Locator.REGISTRATION_BUTTON)
        driver.execute_script("arguments[0].click();", element)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.NAME_INPUT)))
        driver.find_element(By.XPATH, Locator.NAME_INPUT).send_keys(random_credentials['user'])
        driver.find_element(By.XPATH, Locator.EMAIL_INPUT).send_keys(random_credentials['mail'])
        driver.find_element(By.XPATH, Locator.PASS_INPUT).send_keys('12345')
        driver.find_element(By.XPATH, Locator.REGISTRATION_COMMIT_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, Locator.ERROR_LABEL)))
        assert driver.find_element(By.CSS_SELECTOR, Locator.ERROR_LABEL).text == 'Некорректный пароль'