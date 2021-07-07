import requests, random, string, json
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.firefox.options import Options as Firefox_Options
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException
import time

from .bin.settings import Settings
import os, sys

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from emailverification import getmessage
from recaptcha_solver import solver
from datetime import datetime

def random_name():
    url = 'https://api.namefake.com/english-united-states/female/'
    res = requests.get(url)
    data = json.loads(res.text)['name']
    return data.replace(' ', '') + random.choice(string.digits) + random.choice(string.digits) + random.choice(string.digits)

def signup(email):
    username = random_name()
    password = 'Vojko123'
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Length': '556',
        'Cookie': '__cfduid=d96244cfcf984d04435b84c655531867b1614675318; PHPSESSID=svd6331k62tple1qaul0lh8ape',
        'Host': 'adultchat.chat-avenue.com',
        'Origin': 'https://adultchat.chat-avenue.com',
        'Referer': 'https://adultchat.chat-avenue.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0',
        'X-Requested-With': 'XMLHttpRequest'
    }

    data = {
        'password': password,
        'username': username,
        'email': email,
        'age': '21',
        'gender': '2',
        'recaptcha': solver()
    }

    try:
        url = 'https://adultchat.chat-avenue.com/system/encoded/registration.php'
        res = requests.post(url, headers=headers, data=data)
        print(f'[{datetime.now().strftime("%H:%M:%S")}] - Created {email}:{username}:{password}')
    except Exception as e:
        print(f'[{datetime.now().strftime("%H:%M:%S")}] - Error {e}')

def verify(password, email):
    chromedriver_location = Settings.chromedriver_location
    chrome_options = Options()
    #chrome_options.add_argument('headless')
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
    driver = webdriver.Chrome(executable_path=chromedriver_location, options=chrome_options)

    try:
        driver.get('https://adultchat.chat-avenue.com/')
        time.sleep(5)
        login = driver.find_element_by_xpath('//i[@class="fa fa-send"]')
        login.click()
        time.sleep(2)

        usr = driver.find_element_by_xpath('//input[@name="username"]')
        usr.send_keys(email)

        time.sleep(1)

        psw = driver.find_element_by_xpath('//input[@name="password"]')
        psw.send_keys(password)

        time.sleep(1)

        btn = driver.find_element_by_xpath('//button[@class="theme_btn full_button large_button"]')
        btn.click()

        time.sleep(5)

        code = driver.find_element_by_xpath('//input[@id="boom_code"]')
        code.send_keys(getmessage(email))

        time.sleep(5)

        btn = driver.find_element_by_xpath('//button[@class="large_button_rounded ok_btn"]')
        btn.click()

        print(f'[{datetime.now().strftime("%H:%M:%S")}] - Verified')

        driver.close()
        return 'Verified'

    except Exception as e:
        print(f'[{datetime.now().strftime("%H:%M:%S")}] - Error {e}')
        return 'NaN'