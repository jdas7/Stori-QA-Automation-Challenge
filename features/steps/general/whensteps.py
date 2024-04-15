import json
import allure

from allure_commons.types import AttachmentType
from behave import when
from selenium.webdriver.common.alert import Alert

from features.steps.page_objects.modelobjects import AutomationPracticePage
from features.steps.page_objects.webelements.automationpracticepageobjects import AutomationPracticeWebElements

ui = AutomationPracticeWebElements()


@when('I enter the word "{word}" in the option Suggession Class Example')
def enter_word(context, word):
    context.page = AutomationPracticePage(context.browser)
    context.page.find_element_by_xpath(ui.SUGGESTED_CLASS_EXAMPLE).send_keys(word)
    allure.attach(context.browser.get_screenshot_as_png(), name="Suggession Class Example",
                  attachment_type=AttachmentType.PNG)


@when('I selects option 2')
def select_option_2(context):
    context.page = AutomationPracticePage(context.browser)

    context.page.find_element_by_xpath(ui.DROPDOWN_EXAMPLE).click()
    context.page.find_element_by_xpath(ui.DROPDOWN_OPTION_2).click()
    allure.attach(context.browser.get_screenshot_as_png(), name="Select option 2",
                  attachment_type=AttachmentType.PNG)


@when('Then the option 3 in the dropdown example')
def select_option_3(context):
    context.page = AutomationPracticePage(context.browser)

    context.page.find_element_by_xpath(ui.DROPDOWN_OPTION_3).click()
    allure.attach(context.browser.get_screenshot_as_png(), name="Select option 3",
                  attachment_type=AttachmentType.PNG)


@when('I click on the Open Window button in the Switch Window Example')
def clic_open_window(context):
    context.page = AutomationPracticePage(context.browser)

    context.page.clic_by_xpath_with_time_out(ui.OPEN_WINDOW_BUTTON)
    context.page.switch_to_popup_window()
    allure.attach(context.browser.get_screenshot_as_png(), name="Open Window button",
                  attachment_type=AttachmentType.PNG)


@when('I click the Open tab button in the example tab change')
def clic_open_tab(context):
    context.page = AutomationPracticePage(context.browser)

    context.page.find_element_by_css_selector(ui.OPEN_TAP_BUTTON).click()
    context.page.switch_to_popup_window()
    allure.attach(context.browser.get_screenshot_as_png(), name="Open Window button",
                  attachment_type=AttachmentType.PNG)


@when('I navigates to the origin page tab and finds the button')
def find_button(context):
    context.page = AutomationPracticePage(context.browser)

    context.page.switch_to_main_window()
    context.page.scroll_to_element(ui.FRAME)
    context.page.switch_to_frame(ui.FRAME)
    context.page.scroll_to_element(ui.ALL_COURSES)
    allure.attach(context.browser.get_screenshot_as_png(), name="finds the button",
                  attachment_type=AttachmentType.PNG)


@when('I accept the alert and verify the text')
def find_button(context):
    context.page = AutomationPracticePage(context.browser)

    context.page.find_element_by_css_selector(ui.ALERT_BUTTON).click()
    allure.attach(context.browser.get_screenshot_as_png(), name="popup alert",
                  attachment_type=AttachmentType.PNG)

    alert = context.page.switch_to_alert().text
    alert.accept()


@when(u'I repeat the process for the confirmation alert')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I repeat the process for the confirmation alert')


@when('I analyze the courses that cost $25 and $15 in the web table')
def analyze_courses(context):
    context.page = AutomationPracticePage(context.browser)

    context.page.scroll_to_element(ui.SCROLL_TABLE_WEB_EXAMPLE)
    allure.attach(context.browser.get_screenshot_as_png(), name="Table",
                  attachment_type=AttachmentType.PNG)

    table_data = context.page.analyze_table(ui.TABLE_WEB_EXAMPLE)
    json_table_data = json.dumps(table_data, indent=4)

    allure.attach(json_table_data, name="Tabla de cursos", attachment_type=allure.attachment_type.TEXT)


@when('I identify the names of the Engineers and Businessman in the web table')
def analyze_fixed_header_table(context):
    context.page = AutomationPracticePage(context.browser)

    context.page.scroll_to_element(ui.SCROLL_TABLE_WEB_EXAMPLE)
    allure.attach(context.browser.get_screenshot_as_png(), name="Tables",
                  attachment_type=AttachmentType.PNG)

    table_data_json = context.page.analyze_header_table(ui.TABLE_HEADER_WEB_EXAMPLE)
    allure.attach(table_data_json, name="Datos de la tabla", attachment_type=allure.attachment_type.TEXT)


@when('I extract the text in the iFrame')
def extracts_text(context):
    context.page = AutomationPracticePage(context.browser)
    context.page.scroll_to_element(ui.FRAME)
    context.page.switch_to_frame(ui.FRAME)
    context.page.scroll_to_element(ui.TEXT_IFRAME)
    allure.attach(context.browser.get_screenshot_as_png(), name="text in the iFrame",
                  attachment_type=AttachmentType.PNG)
