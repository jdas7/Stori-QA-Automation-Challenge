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


@when('The user selects option 2')
def step_impl(context):
    context.page = AutomationPracticePage(context.browser)

    context.page.find_element_by_xpath(ui.DROPDOWN_EXAMPLE).click()
    context.page.find_element_by_xpath(ui.DROPDOWN_OPTION_2).click()
    allure.attach(context.browser.get_screenshot_as_png(), name="Select option 2",
                  attachment_type=AttachmentType.PNG)


@when('Then the option option 3 in the dropdown example')
def step_impl(context):
    context.page = AutomationPracticePage(context.browser)

    context.page.find_element_by_xpath(ui.DROPDOWN_OPTION_3).click()
    allure.attach(context.browser.get_screenshot_as_png(), name="Select option 3",
                  attachment_type=AttachmentType.PNG)
