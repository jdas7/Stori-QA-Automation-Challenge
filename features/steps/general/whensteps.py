import time

import allure
from allure_commons.types import AttachmentType
from behave import when

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

    context.page.clic_by_xpath_with_time_out(ui.OPEN_TAP_BUTTON)
    context.page.switch_to_popup_window()
    allure.attach(context.browser.get_screenshot_as_png(), name="Open Window button",
                  attachment_type=AttachmentType.PNG)


@when('I navigates to the origin page tab and finds the button')
def clic_open_tab(context):
    context.page = AutomationPracticePage(context.browser)

    context.page.switch_to_main_window()
    context.page.scroll_to_element(ui.FRAME)
    context.page.switch_to_frame(ui.FRAME)
    context.page.scroll_to_element(ui.ALL_COURSES)
    allure.attach(context.browser.get_screenshot_as_png(), name="finds the button",
                  attachment_type=AttachmentType.PNG)
