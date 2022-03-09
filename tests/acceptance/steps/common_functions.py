from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from time import sleep


@when(u'I visited page "{url}"')
def step_impl(context, url):
    # try:
    #     context.driver.get(url)
    # except:
    #     assert False
    # assert True
    if 'http' in url:
        actual_url = url
    else:
        actual_url = context.url_helper(url)
    context.browser.get(actual_url)
    context.url = actual_url


@when(u'Button click by element By ID: "{elem_id}"')
def step_impl(context, elem_id):
    try:
        context.browser.find_element(By.ID, elem_id).click()
        assert True
    except:
        assert False


@when(u'Check redirect to (enter first url part) Url: "{url}"')
def check_redirect_url(context, url):
    sleep(2)
    try:
        current_url = context.browser.current_url
        if current_url.startswith(url):
            assert True
    except:
        assert False


@when(u'Input Text: "{text}" element By ID: "{elem_id}"')
def input_text_id(context, text, elem_id):
    try:
        context.browser.find_element(By.ID, elem_id).send_keys(text)
        assert True
    except:
        assert False


@when(u'Sleep "{sec}" sec')
def input_text_xpath(context, sec):
    try:
        sleep(int(sec))
        assert True
    except:
        assert False
