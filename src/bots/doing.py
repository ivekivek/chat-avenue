from selenium.webdriver.chrome.options import Options
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.firefox.options import Options as Firefox_Options
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException
import time, os

from .bin.settings import Settings
from datetime import datetime

def __init__():
    chromedriver_location = Settings.chromedriver_location
    chrome_options = Options()
    #chrome_options.add_argument('headless')
    chrome_options.add_argument('--mute-audio')
    chrome_options.add_argument('Content-Type="text/html"')
    chrome_options.add_argument('chartset=utf-8')
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-crash-reporter")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-in-process-stack-traces")
    chrome_options.add_argument("--disable-logging")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_argument("--output=/dev/null")
    return webdriver.Chrome(executable_path=chromedriver_location, options=chrome_options)

def login(driver, username, password, pathimg, i):
    print(f'[{datetime.now().strftime("%H:%M:%S")}] - Started {i} Thread')
    
    try:
        driver.get('https://adultchat.chat-avenue.com/')
        time.sleep(5)
        driver.find_element_by_xpath('//button[@class="intro_login_btn large_button_rounded  ok_btn"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//input[@name="username"]').send_keys(username)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[@name="password"]').send_keys(password)
        time.sleep(0.5)
        driver.find_element_by_xpath('//button[@class="theme_btn full_button large_button"]').click()
        time.sleep(5)
        driver.find_element_by_xpath('//div[@id="main_mob_menu"]').click()
        time.sleep(0.5)
        driver.find_element_by_xpath('//div[@class="fmenu_item"]').click()
        time.sleep(5)
        driver.find_element_by_xpath('//input[@id="avatar_image"]').send_keys(os.path.abspath(pathimg))
        time.sleep(0.5)

        driver.get('https://adultchat.chat-avenue.com/')
        time.sleep(10)
    except Exception as e:
        print(f'[{datetime.now().strftime("%H:%M:%S")}] - Error {e}')
    driver.close()

arr = []
done = []
def send_private(driver, message, message_img, link, i):
    try:
        driver.find_element_by_xpath('//div[@id="get_private"]').click()
        time.sleep(2)
        pips = driver.find_elements_by_xpath('/html/body/div[15]/div/div/div[2]/div[1]/div[2]')
        for pip in pips:
            if pip in arr:
                continue
            else:
                arr.append(pip)
        dms = driver.find_elements_by_xpath('//div[@class="ulist_name gprivate"]')
        time.sleep(1)
        for dm in arr:
            if dm in done:
                continue
            dm.click()
            time.sleep(2)
            driver.find_element_by_xpath('//input[@id="private_file"]').send_keys(os.path.abspath(message_img))
            time.sleep(1)
            driver.find_element_by_xpath('//button[@id="private_send"]').click()
            time.sleep(1)
            driver.find_element_by_xpath('//input[@id="message_content"]').send_keys(message)
            time.sleep(1)
            driver.find_element_by_xpath('//input[@id="message_content"]').send_keys(link)
            time.sleep(1)
            driver.find_element_by_xpath('//button[@id="private_send"]').click()
            time.sleep(1)
            print(f'[{datetime.now().strftime("%H:%M:%S")}] - Thread {i}: Private sent')
            done.append(dm)
            driver.find_element_by_xpath('//div[@id="get_private"]').click()
            time.sleep(3)
    except Exception as e:
        print(f'[{datetime.now().strftime("%H:%M:%S")}] - Error {e}')

def send_public(driver, text, i):
    try:
        driver.get('https://adultchat.chat-avenue.com/')
        time.sleep(5)
        driver.find_element_by_xpath('//input[@name="content"]').send_keys(text)
        driver.find_element_by_xpath('//button[@class="default_btn csend"]').click()
        time.sleep(2)
        print(f'[{datetime.now().strftime("%H:%M:%S")}] - Thread {i}: Public sent')
    except Exception as e:
        print(f'[{datetime.now().strftime("%H:%M:%S")}] - Error {e}')

def do(driver, username, password, text, pathimg, message, message_img, link, i):
    login(driver, username, password, pathimg, i)
    while True:
        send_private(driver, message, message_img, link, i)
        send_public(driver, text, i)