import os

from PIL import Image, ImageDraw
import allure
from selenium.webdriver.common.by import By


class ImageUtils:
    @staticmethod
    def highlight_element_in_screenshot(screenshot_path, element_coordinates):
        """
        Resalta un elemento en un screenshot.

        :param screenshot_path: Ruta al screenshot.
        :param element_coordinates: Coordenadas del elemento (x1, y1, x2, y2).
        """
        screenshot = Image.open(screenshot_path)
        draw = ImageDraw.Draw(screenshot)
        draw.rectangle(element_coordinates, outline="red", width=2)

        highlighted_screenshot_path = "highlighted_screenshot.png"
        screenshot.save(highlighted_screenshot_path)

        allure.attach.file(highlighted_screenshot_path, name="Highlighted Screenshot",
                           attachment_type=allure.attachment_type.PNG)

    @staticmethod
    def get_element_coordinates(driver, xpath):
        """
        Obtiene las coordenadas (x1, y1, x2, y2) de un elemento dado su XPath.

        :param driver: Instancia del driver de Selenium.
        :param xpath: XPath del elemento.
        :return: Coordenadas (x1, y1, x2, y2) del elemento.
        """
        element = driver.find_element(By.XPATH, xpath)
        location = element.location
        size = element.size
        x1 = location['x']
        y1 = location['y']
        x2 = x1 + size['width']
        y2 = y1 + size['height']
        return x1, y1, x2, y2

    @staticmethod
    def attach_screenshot_to_allure(driver, name="expected result"):
        """
        Adjunta un screenshot al reporte de Allure y devuelve la ruta del screenshot.

        :param driver: Instancia del driver de Selenium.
        :param name: Nombre del screenshot (por defecto "screenshot").
        :return: Ruta del screenshot adjuntado.
        """
        screenshot_bytes = driver.get_screenshot_as_png()
        screenshot_name = f"{name}.png"
        screenshot_path = os.path.join(os.getcwd(), screenshot_name)

        with open(screenshot_path, "wb") as file:
            file.write(screenshot_bytes)

        allure.attach.file(screenshot_path, name="expected result", attachment_type=allure.attachment_type.PNG)
        return screenshot_path

    @staticmethod
    def attach_text_to_allure(text, name):
        allure.attach(text, name, allure.attachment_type.TEXT)
