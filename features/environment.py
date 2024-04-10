from selenium import webdriver


def before_all(context):
    browser_name = context.config.userdata.get("browser", "chrome")

    if browser_name.lower() == "chrome":
        context.browser = webdriver.Chrome()
    elif browser_name.lower() == "firefox":
        context.browser = webdriver.Firefox()
    elif browser_name.lower() == "opera":
        context.browser = webdriver.Opera()
    else:
        raise ValueError(f"Invalid browser name: {browser_name}")

    context.browser.maximize_window()
    context.browser.implicitly_wait(5)


def after_all(context):
    context.browser.quit()
