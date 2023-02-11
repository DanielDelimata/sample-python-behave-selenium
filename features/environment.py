import os
from xml.etree.cElementTree import Element, SubElement, ElementTree

import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from features.lib.pages.customers_page import CustomersPage


def before_scenario(context, scenario):
    options = Options()
    options.headless = True
    options.add_argument('--headless')
    context.base_url = 'http://'
    context.driver = webdriver.Chrome(options=options)
    context.customers_page = CustomersPage(context)


def after_scenario(context, scenario):
    if scenario.status == "failed":
        allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    context.driver.quit()


def before_all(context):
    allure_results_dir = os.path.join("../../allure_results")
    os.makedirs(allure_results_dir, exist_ok=True)
    environment = Element("environment")
    for key, value in os.environ.items():
        param = SubElement(environment, "parameter")
        SubElement(param, "key").text = key
        SubElement(param, "value").text = value
    ElementTree(environment).write(os.path.join(allure_results_dir, "environment.xml"))
