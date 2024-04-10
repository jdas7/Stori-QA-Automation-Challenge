import allure
import logging

from behave import given
from allure_commons.types import AttachmentType

from features.steps.page_objects.pageobjects import AutomationPracticePage

logger = logging.getLogger(__name__)


@given(u'I access the page "{url}"')
def step_impl(context, url):
    logger.debug('url page', url)
    context.browser.get(url)
    allure.attach(context.browser.get_screenshot_as_png(), name="home_page", attachment_type=AttachmentType.PNG)


@given(u'I navigate to the AutomationPractice main page')
def step_impl(context):
    context.page = AutomationPracticePage(context.browser)
    context.page.open()
    allure.attach(context.browser.get_screenshot_as_png(), name="home_page", attachment_type=AttachmentType.PNG)
