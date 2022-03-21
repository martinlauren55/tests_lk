import sys

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import ntpath
import os
from sys import platform
from selenium.common.exceptions import NoSuchElementException

from time import sleep

if platform == "linux" or platform == "linux2":
    # linux
    # path_to_driver = os.path.join(ntpath.dirname(__file__), os.path.join("venv/lib/python3.8/site-packages/seleniumbase/drivers/chromedriver"))  # for lin
    path_to_driver = os.path.join(ntpath.dirname(__file__), os.path.join("chromedriver"))  # for lin
    s = Service(path_to_driver)  # for lin
    browser = webdriver.Chrome(service=s)  # for lin

elif platform == "darwin":
    # OS X
    print(f'no driver for this platform: {platform}')
elif platform == "win32":
    # Windows...
    path_to_driver = os.path.join(ntpath.dirname(__file__), os.path.join("chromedriver.exe"))  # for win
    s = Service(path_to_driver)  # for win
    options = webdriver.ChromeOptions()  # for win
    options.add_experimental_option('excludeSwitches', ['enable-logging'])  # for win
    browser = webdriver.Chrome(service=s, options=options)  # for win

browser.implicitly_wait(15)


def login():
    browser.get("http://217.9.89.223")
    # get_web_element_from_dict(browser, browser.find_element(By.ID, "login")).click()
    browser.find_element(By.ID, "login").click()
    browser.find_element(By.ID, "username").send_keys("test_user_13@inbox.ru")
    browser.find_element(By.ID, "password").send_keys("2ij-4ZR-Lpt-yhS")
    browser.find_element(By.ID, "kc-login").click()


login()
browser.find_element(By.XPATH, "/html/body/div[3]/div/main/div/div[2]/div[2]/div/div/div[2]/div/div/div").click()
browser.find_element(By.XPATH, "/html/body/div[5]/div/div/form/div[2]/div/div/div/div[1]/div[1]").click()

# And I select "БЕЛАРУСЬ" as country
def step_implementation(value, item):
    sleep(1)
    try:
        select = browser.find_element(By.ID, item)
    except NoSuchElementException:
        item = browser.find_element(By.XPATH, f'//div[contains(.,"{value}") and contains(@class, "radio")]')
        item.click()
        return
    select.click()
    sleep(1)
    items = browser.find_elements(By.XPATH, f'//div[contains(.,"{value}")]')
    assert items
    print(items, file=sys.stderr)
    for item in items:
        inner = item.get_attribute('innerHTML')
        if inner.strip() == value:
            break
    print(item.get_attribute('innerHTML'), file=sys.stderr)
    item.click()
    sleep(1)

step_implementation("БЕЛАРУСЬ", "country")
