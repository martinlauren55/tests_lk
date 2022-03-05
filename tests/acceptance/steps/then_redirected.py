from urllib.parse import urlparse

from behave import then
from selenium.webdriver.support.ui import WebDriverWait


@then("I should be redirected to {url}")
def step_implementation(context, url):
    wait = WebDriverWait(context.browser, 10)
    if 'http' in url:
        expected = url
    else:
        expected = context.url_helper(url)
    print(expected)
    print(context.browser.current_url)
    wait.until(lambda browser: _path(browser.current_url) == _path(expected))


@then("I should be redirected")
def step_implementation(context):
    url = context.url
    wait = WebDriverWait(context.browser, 10)
    print("url, ", context.browser.current_url)
    print("just url, ", url)
    wait.until(lambda browser: browser.current_url != url)


@then("I should not be redirected")
def step_implementation(context):
    url = context.url
    # TODO reconsider this check into
    # something less naive
    context.browser.implicitly_wait(2)
    print(context.browser.current_url)
    assert context.browser.current_url == url

# @then("I should be redirected to keycloak authorization page")
# def step_implementation(context):
#     url = context.url
#     # TODO reconsider this check into
#     # something less naive
#     context.browser.implicitly_wait(2)
#     print("aaaaa", context.browser.current_url)
#     assert context.browser.current_url == url


def _path(url):
    return urlparse(url).path
