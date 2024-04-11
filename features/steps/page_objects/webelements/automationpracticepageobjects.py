class AutomationPracticeWebElements:
    TITTLE = '/html/body/h1'
    SUGGESTED_CLASS_EXAMPLE = '//*[@id="autocomplete"]'
    DROPDOWN_EXAMPLE = '//*[@id="dropdown-class-example"]'
    DROPDOWN_OPTION_2 = '//*[@id="dropdown-class-example"]/option[3]'
    DROPDOWN_OPTION_3 = '//*[@id="dropdown-class-example"]/option[4]'

    selector_mapping = {
        "México": {
            "xpath": '//*[@id="ui-id-1"]/li[6]'
        },
        "Estados Unidos": {
            "xpath": '//*[@id="ui-id-1"]/li[6]'
        },
        "Emiratos Árabes Unidos": {
            "xpath": '//*[@id="ui-id-1"]/li[4]'
        },
        "Colombia": {
            "xpath": '//*[@id="ui-id-1"]/li'
        }
    }
