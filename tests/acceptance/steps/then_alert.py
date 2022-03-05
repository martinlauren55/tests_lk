from behave import then


@then("alert window is present")
def step_implementation(context):
    from datetime import datetime
    browser = context.browser
    browser.save_screenshot(f"/screenshots/alert-{datetime.now()}.png")
    browser.switch_to.alert.accept()
