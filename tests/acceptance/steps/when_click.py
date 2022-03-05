from behave import when
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@when("I click \"{text}\"")
def step_implementation(context, text):
    from time import sleep
    from datetime import datetime
    import sys
    sleep(1)
    wait = WebDriverWait(context.browser, 50)
    context.browser.save_screenshot(f"/screenshots/{datetime.now()}.png")
    print(context.browser.find_element_by_tag_name("body").text, file=sys.stderr)
    try:
        element = context.browser.find_element_by_partial_link_text(text)
    except NoSuchElementException:
        try:
            element = context.browser.find_element_by_xpath(f'//*[contains(text(),"{text}")]')
        except NoSuchElementException:
            element = context.browser.find_element_by_xpath(f'//div[contains(text(),"{text}")]')
            #element = context.browser.find_element_by_id(text)
            #element = context.browser.find_element_by_xpath(f'//input[@value="{text}" and @type="button"]')
    try:
        element.click()
    except ElementNotInteractableException:
        element = wait.until(
            EC.presence_of_element_located((By.XPATH, f'//div[contains(text(),"{text}")]')))
        element.click()




