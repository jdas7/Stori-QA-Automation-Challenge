import allure

from behave import given
from allure_commons.types import AttachmentType

from features.steps.page_objects.modelobjects import AutomationPracticePage


@given(u'I access the page "{url}"')
def step_impl(context, url):
    context.browser.get(url)
    allure.attach(context.browser.get_screenshot_as_png(), name="Home page", attachment_type=AttachmentType.PNG)


@given(u'I navigate to the AutomationPractice main page')
def step_impl(context):
    context.page = AutomationPracticePage(context.browser)
    context.page.open()
    allure.attach(context.browser.get_screenshot_as_png(), name="Home page", attachment_type=AttachmentType.PNG)
