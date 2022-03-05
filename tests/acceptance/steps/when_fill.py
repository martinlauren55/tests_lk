from behave import when


@when("I fill {field} with {value}")
def step_implementation(context, field, value):
    from time import sleep
    sleep(0.1)
    browser_field = context.browser.find_element_by_name(field)
    if value.startswith("my"):
        value = value.removeprefix("my ")
        value = getattr(context.user, value)
    else:
        value = value.strip("\"")
    browser_field.send_keys(value)


@when("I fill my {information_type} information")
def step_implementation(context, information_type):
    from time import sleep
    sleep(0.1)
    form_filler = context.form_filler
    information = getattr(context.user, information_type)
    for key in vars(information):
        value = getattr(information, key)
        if information_type == "passport":
            key = f"passport.{key}"
        if information_type == "address":
            key = f"address.{key}"
        form_filler.fill(key, value)
