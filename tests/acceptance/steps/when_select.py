from behave import when
from selenium.common.exceptions import NoSuchElementException


@when('I select "{value}" as {item}')
def step_implementation(context, value, item):
    import sys
    from datetime import datetime
    from time import sleep
    sleep(0.1)
    browser = context.browser
    try:
        select = browser.find_element_by_id(item)
    except NoSuchElementException:
        item = browser.find_element_by_xpath(f'//div[contains(.,"{value}") and contains(@class, "radio")]')
        item.click()
        return
    select.click()
    sleep(0.1)
    context.browser.save_screenshot(f"/screenshots/select{datetime.now()}.png")
    items = browser.find_elements_by_xpath(f'//div[contains(.,"{value}")]')
    assert items
    print(items, file=sys.stderr)
    for item in items:
        inner = item.get_attribute('innerHTML')
        if inner.strip() == value:
            break
    print(item.get_attribute('innerHTML'), file=sys.stderr)
    context.browser.save_screenshot(f"/screenshots/select2{datetime.now()}.png")
    item.click()
    sleep(0.1)
    context.browser.save_screenshot(f"/screenshots/select3{datetime.now()}.png")
