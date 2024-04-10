from behave import then


@then(u'I see the option Suggession Class Example')
def step_impl(context):
    pass


@then('I select the country "{country}" correctly')
def select_country(context, country):
    # Implementación para seleccionar el país correcto en la lista desplegable
    print(country)
    pass
