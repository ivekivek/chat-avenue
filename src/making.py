import requests
import random
import string
import json

from selenium.webdriver.chrome.options import Options
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.firefox.options import Options as Firefox_Options
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException
import time

from .emailverification import getaddress, getmessage
from .recaptcha_solver import solver

import os
from sys import platform as p_os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OS_ENV = "windows" if p_os == "win32" else "osx" if p_os == "darwin" else "linux"

class Settings:

    chromedriver_min_version = 2.36

    specific_chromedriver = "chromedriver_{}".format(OS_ENV)
    chromedriver_location = os.path.join(BASE_DIR, "assets", specific_chromedriver)

    if not os.path.exists(chromedriver_location):
        chromedriver_location = os.path.join(BASE_DIR, 'assets', 'chromedriver')

chromedriver_location = Settings.chromedriver_location

#def random_name():  return ''.join(random.choice(string.ascii_letters) for i in range(8))
def random_name():
    #import json
    #import requests
    #import random
    #import string
    url = 'https://api.namefake.com/english-united-states/female/'
    res = requests.get(url)
    data = json.loads(res.text)['name']
    return data.replace(' ', '') + random.choice(string.digits) + random.choice(string.digits) + random.choice(string.digits)
#print(random_name())

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
        'age': '46',
        'gender': '2',
        'recaptcha': solver()
    }

    try:
        url = 'https://adultchat.chat-avenue.com/system/encoded/registration.php'
        res = requests.post(url, headers=headers, data=data)
        print('Created!')
        print(email)
        print(username)
        print(password)
        #print(res.text)
    except Exception as e:
        print(e)

def verify(password, email):
    chrome_options = Options()
    chrome_options.add_argument('headless')
    chrome_options.add_argument('Content-Type="text/html"')
    chrome_options.add_argument('chartset=utf-8')
    driver = webdriver.Chrome(executable_path=chromedriver_location, chrome_options=chrome_options)

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

        print('Verified!')

        driver.close()

    except Exception as e:
        print(e)

def guestsignin():
    username = random_name()
    print(username)
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
        'guest_name': username,
        'guest_gender': '1',
        'guest_age': '1',
        'recaptcha': gettoken()
    }

    try:
        url = 'https://adultchat.chat-avenue.com/system/encoded/registration.php'
        s = requests.session()
        res = s.post(url, headers=headers, data=data)

        while True:
            res2 = s.post('https://adultchat.chat-avenue.com/system/chat_process.php', data={'content': 'How are you?'})
            time.sleep(1)
    except Exception as e:
        print(e)