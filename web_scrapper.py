import sys
import threading
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import atexit
import props

browser = object()
robot_busy = False


def open_browser():
    global browser
    try:
        opts = webdriver.ChromeOptions()
        # opts.add_argument("--no-sandbox")
        opts.add_argument("--window-size=1420,1080")
        # opts.add_argument("--headless")
        opts.add_argument("--disable-gpu")
        browser = webdriver.Chrome(chrome_options=opts)
    except Exception as e:
        print(e.with_traceback)

def open_page():
    global browser
    browser.get(props.url)
    search_elem = browser.find_elements(
            By.ID, props.search_path)[0]
    search_elem.clear()
    search_elem.send_keys("korona son haberler")
    search_button = browser.find_elements(
            By.ID, props.search_button)[0]
    search_button.click()
    time.sleep(3)
    first_result_elem = browser.find_elements(
            By.ID, props.first_result_link)[0]
    link_address = first_result_elem.get_attribute['href']
    browser.get(link_address)
    

def quit():
    global browser
    if browser:
        browser.quit()


atexit.register(quit)
open_browser()
open_page()