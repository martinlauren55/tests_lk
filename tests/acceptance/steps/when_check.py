from behave import when


@when("I check personal data processing agreement")
def step_implementation(context):
    element = context.browser.find_element_by_id("personal_data_processing_agreement")
    element.click()


@when("I check dormitory")
def step_implementation(context):
    element = context.browser.find_element_by_id("need_dormitory")
    element.click()


@when("I check no address")
def step_implementation(context):
    element = context.browser.find_element_by_id("no_address")
    element.click()
