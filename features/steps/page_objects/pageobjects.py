import time

from selenium.webdriver.common.by import By


class AutomationPracticePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://rahulshettyacademy.com/AutomationPractice/"
        self.input_field = (By.ID, "name")

    def open(self):
        self.driver.get(self.url)

    def enter_text_and_select_option(self, text, option):
        input_field = self.driver.find_element(*self.input_field)
        input_field.send_keys(text)
        time.sleep(2)  # Asegurémonos de esperar a que aparezca la lista de opciones
        option_xpath = f"//*[text()='{option}']"
        option_element = self.driver.find_element(By.XPATH, option_xpath)
        option_element.click()
