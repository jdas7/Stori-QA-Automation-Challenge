class AutomationPracticeWebElements:
    TITTLE = '/html/body/h1'
    SUGGESTED_CLASS_EXAMPLE = '//*[@id="autocomplete"]'

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
