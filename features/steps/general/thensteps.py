from behave import then

from features.steps.page_objects.modelobjects import AutomationPracticePage
from features.steps.page_objects.webelements.automationpracticepageobjects import AutomationPracticeWebElements
from utils.allureutils import ImageUtils

ui = AutomationPracticeWebElements()


@then(u'I see the option Suggession Class Example')
def step_impl(context):
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

