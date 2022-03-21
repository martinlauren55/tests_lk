# import os
# from time import sleep
#
# from selenium import webdriver
# from selenium.webdriver import DesiredCapabilities
# from selenium.common.exceptions import UnexpectedAlertPresentException
# from steps.utils.mailbox import Mailbox
# from steps.utils.form import FormFiller
#
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
#
# import ntpath
# import os

# def before_tag(context, tag):
#     if tag == "browser":
#         host = "selenium-hub"
#         port = 4444
#         browser = webdriver.Remote(
#             command_executor=(f"http://{host}:{port}/wd/hub"),
#             desired_capabilities=DesiredCapabilities.FIREFOX,
#         )
#         context.browser = browser
#         context.url_helper = lambda s: f"http://webserver{s}"
#         context.form_filler = FormFiller(context.browser)


# path_to_driver = os.path.join(ntpath.dirname(__file__), os.path.join("chromedriver"))
# s = Service(path_to_driver)   # for lin
# driver = webdriver.Chrome(service=s)   # for lin

# 33333333333333333333333333333333333333333333333333333333333
# host = "172.17.0.3"
# port = 4444
# browser = webdriver.Remote(
#     command_executor=(f"http://{host}:{port}/wd/hub"),
#     desired_capabilities=DesiredCapabilities.CHROME,
# )
# driver = browser
# driver.url_helper = lambda s: f"http://webserver{s}"
# form_filler = FormFiller(driver)



# _________
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

firefox_options = webdriver.ChromeOptions()
driver = webdriver.Remote(
    command_executor='http://172.17.0.2:4444',
    options=firefox_options
)
sleep(15)
driver.get('https://vk.com/')
print(driver.find_element(By.CLASS_NAME, "login_mobile_header").text)
sleep(5)
driver.get('https://vk.com/about')

sleep(15)





driver.quit()

# +++++++++++++++++++++++++++++++++
# from selenium import webdriver
#
# chrome_options = webdriver.ChromeOptions()
# chrome_options.set_capability("browserVersion", "67")
# chrome_options.set_capability("platformName", "Windows XP")
# driver = webdriver.Remote(
#     command_executor='http://www.example.com',
#     options=chrome_options
# )
# driver.get("http://www.google.com")
# driver.quit()
