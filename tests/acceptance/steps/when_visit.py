from behave import when


@when("I visit {url}")
def step_implementation(context, url):
    if 'http' in url:
        actual_url = url
    else:
        actual_url = context.url_helper(url)
    context.browser.get(actual_url)
    context.url = actual_url
