from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from locators import Locator

class TestExit():

    def test_exit_from_account_page_and_transition_to_main_page_return_enter_account_button(self, driver, credentials):
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.ACCOUNT_BUTTON)))
        element = driver.find_element(By.XPATH, Locator.ACCOUNT_BUTTON)
        driver.execute_script("arguments[0].click();", element)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.LOGIN_BUTTON)))
        driver.find_element(By.XPATH, Locator.EMAIL_INPUT).send_keys(credentials['mail'])
        driver.find_element(By.XPATH, Locator.PASS_INPUT).send_keys(credentials['password'])
        driver.find_element(By.XPATH, Locator.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.ACCOUNT_BUTTON)))
        element = driver.find_element(By.XPATH, Locator.ACCOUNT_BUTTON)
        driver.execute_script("arguments[0].click();", element)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.EXIT_BUTTON)))
        element = driver.find_element(By.XPATH, Locator.EXIT_BUTTON)
        driver.execute_script("arguments[0].click();", element)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.STELLAR_BURGET_BUTTON[0])))
        element = driver.find_element(By.XPATH, Locator.STELLAR_BURGET_BUTTON[0]).find_element(By.XPATH, Locator.STELLAR_BURGET_BUTTON[1])
        driver.execute_script("arguments[0].click();", element)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.CREATE_ORDER_BUTTON)))
        assert driver.find_element(By.XPATH, Locator.CREATE_ORDER_BUTTON) is not None