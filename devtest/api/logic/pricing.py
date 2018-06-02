from api.logic import PricingLogic
from bs4 import BeautifulSoup
from selenium import webdriver
import urllib.request
import json
import platform
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from api.logic import price, recur_collection_search, ilen
import shutil
from selenium.common.exceptions import NoSuchElementException


web_timeout_in_seconds = 20


options = webdriver.ChromeOptions()
if platform.system() == 'Windows':
    options.binary_location = 'C:\\Users\\oskar\\AppData\\Local\\Google\\Chrome SxS\\Application\\chrome.exe'
    chrome_driver_binary = 'C:\\Temp\\chromedriver.exe'
else:
    options.binary_location = shutil.which('chrome')  # Ask OS where is the chrome binary
    if options.binary_location is None:
        options.binary_location = '/usr/bin/google-chrome-stable'

    chrome_driver_binary = shutil.which('chromedriver')  # Again, ask OS for path to chrome-driver
    if chrome_driver_binary is None:
        chrome_driver_binary = '/usr/lib/chromium-browser/chromedriver'

    # Travis CI specific
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--headless')
    # options.add_argument('--no-sandbox')


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

        try:
            # Wait for any popups to go away - wait no more than web_timeout_in_seconds
            element = WebDriverWait(driver, web_timeout_in_seconds).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.btn')))
            # Skipping the GDPR protection
            element.click()
            # Wait for the site to fully load
            time.sleep(5)
        except (NoSuchElementException, TimeoutException):
            pass
            # This is expected behaviour - GDPR notice may be disabled if we're whitelisted

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
            result = recur_collection_search(data)
            return ilen(result)


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

        # Let the site fully load
        time.sleep(15)

        try:
            # Wait for any popups to go away - wait no more than web_timeout_in_seconds
            element = WebDriverWait(driver, web_timeout_in_seconds).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.btn')))
            # Skipping the GDPR protection
            element.click()
            # Wait for the site to fully load
            time.sleep(5)
        except (NoSuchElementException, TimeoutException):
            pass
            # This is expected behaviour - GDPR notice may be disabled if we're whitelisted

        soup = BeautifulSoup(driver.page_source, "html.parser")
        count_tags = len([tag for tag in soup.findAll()])
        return count_tags / 100
