from api.logic import PricingLogic
from bs4 import BeautifulSoup
from selenium import webdriver
import urllib.request
import json
import platform
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from api.logic import price, recur_array_search


web_timeout_in_seconds = 20


options = webdriver.ChromeOptions()
if platform.system() == 'Windows':
    options.binary_location = 'C:\\Users\\oskar\\AppData\\Local\\Google\\Chrome SxS\\Application\\chrome.exe'
    chrome_driver_binary = 'C:\\Temp\\chromedriver.exe'
else:
    options.binary_location = '/usr/bin/google-chrome'
    chrome_driver_binary = '/usr/lib/chromium-browser/chromedriver'


class FirstPricingLogic(PricingLogic):

    panel_id = 'time dot com'

    def __init__(self):

        self.panel_id = FirstPricingLogic.panel_id

        # singleton - parse price just once
        if self.panel_id not in price:

            print('FirstPricingLogic is computing the price... please wait!')
            # do calculations
            price[self.panel_id] = FirstPricingLogic._do_scrapping(webdriver.Chrome(chrome_driver_binary,
                                                                   chrome_options=options))

        else:
            # price is already there, woohoo!
            pass

    @staticmethod
    def _do_scrapping(driver):
        driver.get('http://time.com/')

        # Let the site fully load
        time.sleep(15)
        # element_to_be_clickable is not always reliable due to cookie popups etc
        element = WebDriverWait(driver, web_timeout_in_seconds).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.btn')))

        # Skipping the GDPR protection
        element.click()

        time.sleep(5)
        how_many = driver.find_element_by_tag_name('body').text.count('a')
        return how_many / 100


class SecondPricingLogic(PricingLogic):

    panel_id = 'open library'

    def __init__(self):
        self.panel_id = SecondPricingLogic.panel_id

        if self.panel_id not in price:

            print('SecondPricingLogic is computing the price... please wait!')
            price[self.panel_id] = SecondPricingLogic._do_parsing()

    @staticmethod
    def _do_parsing():
        with urllib.request.urlopen("http://openlibrary.org/search.json?q=the+lord+of+the+rings") as url:
            data = json.loads(url.read().decode())
            result = recur_array_search(data)
            return len(list(result))


class ThirdPricingLogic(PricingLogic):

    panel_id = 'time dot com [alt]'

    def __init__(self):

        self.panel_id = ThirdPricingLogic.panel_id

        if self.panel_id not in price:

            print('ThirdPricingLogic is computing the price... please wait!')
            price[self.panel_id] = ThirdPricingLogic._do_scrapping(webdriver.Chrome(chrome_driver_binary,
                                                                   chrome_options=options))

    @staticmethod
    def _do_scrapping(driver):
        driver.get('http://time.com/')
        time.sleep(15)
        element = WebDriverWait(driver, web_timeout_in_seconds).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.btn')))
        element.click()
        time.sleep(5)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        count_tags = len([tag for tag in soup.findAll()])
        return count_tags / 100
