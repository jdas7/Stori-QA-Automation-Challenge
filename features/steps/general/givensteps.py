import allure

from behave import given
from allure_commons.types import AttachmentType

from features.steps.page_objects.modelobjects import AutomationPracticePage
from features.steps.page_objects.webelements.automationpracticepageobjects import AutomationPracticeWebElements

ui = AutomationPracticeWebElements()


@given(u'I access the page "{url}"')
def home_page(context, url):
    context.browser.get(url)
    allure.attach(context.browser.get_screenshot_as_png(), name="Home page", attachment_type=AttachmentType.PNG)


@given(u'I navigate to the AutomationPractice main page')
def main_page(context):
    context.page = AutomationPracticePage(context.browser)
    context.page.open()
    allure.attach(context.browser.get_screenshot_as_png(), name="Home page", attachment_type=AttachmentType.PNG)


@given('type the string "Stori Card" in the example Change to alert')
def main_page(context):
    context.page = AutomationPracticePage(context.browser)
    context.page.find_element_by_xpath(ui.ENTER_ALERT).send_keys("Stori Card")
    allure.attach(context.browser.get_screenshot_as_png(), name="Suggession Class Example",
                  attachment_type=AttachmentType.PNG)
