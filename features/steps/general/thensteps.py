import json

import allure
from behave import then
from selenium.common import NoSuchElementException

from features.steps.page_objects.modelobjects import AutomationPracticePage
from features.steps.page_objects.webelements.automationpracticepageobjects import AutomationPracticeWebElements
from utils.allureutils import ImageUtils

ui = AutomationPracticeWebElements()


@then(u'I see the option Suggession Class Example')
def suggession_class(context):
    expected_text = "Practice Page"

    context.page = AutomationPracticePage(context.browser)
    actual_text = context.page.assert_text_by_xpath(ui.TITTLE)

    assert actual_text == expected_text, f"Expected text: {expected_text}, Actual text: {actual_text}"

    ImageUtils.attach_text_to_allure(expected_text, "Expected Text")
    ImageUtils.attach_text_to_allure(actual_text, "Actual Text")
    screenshot_path = ImageUtils.attach_screenshot_to_allure(context.browser, name="home_page")
    element_coordinates = ImageUtils.get_element_coordinates(context.browser, ui.TITTLE)
    ImageUtils.highlight_element_in_screenshot(screenshot_path, element_coordinates)


@then('I select the country "{country}" correctly')
def select_country(context, country):
    context.page = AutomationPracticePage(context.browser)

    xpath = AutomationPracticeWebElements.selector_mapping[country]["xpath"]
    context.page.find_element_by_xpath(xpath).click()

    screenshot_path = ImageUtils.attach_screenshot_to_allure(context.browser, name="suggested class example")
    element_coordinates = ImageUtils.get_element_coordinates(context.browser, ui.SUGGESTED_CLASS_EXAMPLE)
    ImageUtils.highlight_element_in_screenshot(screenshot_path, element_coordinates)


@then('I verifies the change in the selection')
def change_option(context):
    context.page = AutomationPracticePage(context.browser)

    actual_text = context.page.assert_text_by_xpath(ui.DROPDOWN_EXAMPLE)

    ImageUtils.attach_text_to_allure(actual_text, "Actual Text")

    screenshot_path = ImageUtils.attach_screenshot_to_allure(context.browser, name="Dropdown Example")
    element_coordinates = ImageUtils.get_element_coordinates(context.browser, ui.DROPDOWN_EXAMPLE)
    ImageUtils.highlight_element_in_screenshot(screenshot_path, element_coordinates)


@then('I verifies that the "30 day money back guarantee" text is displayed')
def verify_text(context):
    context.page = AutomationPracticePage(context.browser)

    try:
        element = context.page.find_element_by_xpath(ui.TEXT)

        assert element.is_displayed(), "El texto '30 day money back guarantee' no está visible en la página."
        ImageUtils.attach_screenshot_to_allure(context.browser, name="30 day money back guarantee")
    except NoSuchElementException:
        raise AssertionError("Failed: El texto '30 day money back guarantee' no se encuentra en la página.")
    finally:
        context.page.switch_to_main_window()


@then('I captures a screenshot that includes the button and saves it with the test case name')
def verify_text(context):
    screenshot_path = ImageUtils.attach_screenshot_to_allure(context.browser,
                                                             name="check navigation and capture screen in new tab")
    element_coordinates = ImageUtils.get_element_coordinates(context.browser, ui.ALL_COURSES)
    ImageUtils.highlight_element_in_screenshot(screenshot_path, element_coordinates)


@then('I print the names of the courses and their corresponding prices')
def print_course_names_and_prices(context):
    context.page = AutomationPracticePage(context.browser)

    table_data = context.page.analyze_table(ui.TABLE_WEB_EXAMPLE)
    course_info = context.page.print_course(table_data)

    allure.attach(course_info, name="courses and their corresponding prices",
                  attachment_type=allure.attachment_type.TEXT)

    count_25 = 0
    names_25 = []
    for course in table_data:
        if course['Price'] == '25':
            count_25 += 1
            names_25.append(course['Course'])
    allure.attach("\n".join(names_25), name="Cursos que cuestan $25", attachment_type=allure.attachment_type.TEXT)

    count_15 = 0
    names_15 = []
    for course in table_data:
        if course['Price'] == '15':
            count_15 += 1
            names_15.append(course['Course'])

    allure.attach("\n".join(names_15), name="Cursos que cuestan $15", attachment_type=allure.attachment_type.TEXT)


@then('I print the names identifying the role')
def print_names(context):
    context.page = AutomationPracticePage(context.browser)

    table_data_json = context.page.analyze_header_table(ui.TABLE_HEADER_WEB_EXAMPLE)
    table_data = json.loads(table_data_json)

    engineers = []
    entrepreneurs = []

    for row in table_data:
        if row['Position'] == 'Engineer':
            engineers.append(row['Name'])
        elif row['Position'] == 'Businessman':
            entrepreneurs.append(row['Name'])

    allure.attach(f"Nombres de los Ingenieros: {', '.join(engineers)}", name="Ingenieros",
                  attachment_type=allure.attachment_type.TEXT)
    allure.attach(f"Nombres de los Empresarios: {', '.join(entrepreneurs)}", name="Empresarios",
                  attachment_type=allure.attachment_type.TEXT)

