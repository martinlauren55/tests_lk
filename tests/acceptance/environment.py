from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import ntpath
import os

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def before_all(context):
    ip_adr = "172.17.0.2"
    port = 4444
    browser_options = webdriver.ChromeOptions()
    context.browser = webdriver.Remote(command_executor=f'http://{ip_adr}:{port}', options=browser_options)

    # path_to_driver = os.path.join(ntpath.dirname(__file__), os.path.join("chromedriver"))
    # s = Service(path_to_driver)   # for lin
    # context.browser = webdriver.Chrome(service=s)   # for lin
#
#
def after_all(context):
    context.browser.quit()
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ========================================


# def before_all(context):
#     ip_adr = "172.17.0.2"
#     port = 4444
#     browser_options = webdriver.ChromeOptions()
#     context.browser = webdriver.Remote(command_executor=f'http://{ip_adr}:{port}/wd/hub', options=browser_options)
#
#     # path_to_driver = os.path.join(ntpath.dirname(__file__), os.path.join("chromedriver"))
#     # s = Service(path_to_driver)   # for lin
#     # context.browser = webdriver.Chrome(service=s)   # for lin
#
#
# def after_all(context):
#     context.browser.quit()


# ========================================