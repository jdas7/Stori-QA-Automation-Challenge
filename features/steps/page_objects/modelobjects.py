import time

from selenium.common import NoSuchWindowException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class AutomationPracticePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://rahulshettyacademy.com/AutomationPractice/"
        self.input_field = (By.ID, "name")
        self.original_window = None

    def open(self):
        self.driver.get(self.url)

    def find_element_by_css_selector(self, css_selector):
        return self.driver.find_element(By.CSS_SELECTOR, css_selector)

    def find_element_by_xpath(self, xpath):
        return self.driver.find_element(By.XPATH, xpath)

    def assert_text_by_xpath(self, xpath):
        element = self.driver.find_element(By.XPATH, xpath)
        return element.text

    def clic_by_xpath_with_time_out(self, xpath):
        self.driver.find_element(By.XPATH, xpath).click()
        time.sleep(10)

    def switch_to_popup_window(self):
        self.original_window = self.driver.current_window_handle
        try:
            self.driver.switch_to.window(self.driver.window_handles[1])
        except NoSuchWindowException:
            print("No se encontró una ventana emergente.")

    def switch_to_frame(self, frame_selector):
        iframe = self.driver.find_element(By.XPATH, frame_selector)

        self.driver.switch_to.frame(iframe)

    def switch_to_main_window(self):
        self.driver.switch_to.window(self.driver.window_handles[0])

    def scroll_to_element(self, xpath):
        element = self.driver.find_element(By.XPATH, xpath)

        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
