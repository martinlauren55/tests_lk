from behave import when
import random


@when("I select {n} specialities")
def step_implementation(context, n):
    import time
    time.sleep(0.1)
    n = int(n)
    for _ in range(n):
        select_unselected_speciality(context.browser)
        time.sleep(0.1)


@when("I select 1 speciality")
def step_implementation(context):
    import time
    time.sleep(0.1)
    select_unselected_speciality(context.browser)


def select_unselected_speciality(browser):
    specialities = browser.find_elements_by_css_selector(
        ".speciality:not(.speciality--selected)",
    )
    speciality = random.choice(specialities)
    speciality.click()
