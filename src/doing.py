from tkinter.constants import NONE
import requests
from harvester import fetch
from harvester import Harvester
import random
import string

from selenium.webdriver.chrome.options import Options
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.firefox.options import Options as Firefox_Options
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException
import time

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
chrome_options = Options()
chrome_options.add_argument('headless')
chrome_options.add_argument('--mute-audio')
chrome_options.add_argument('Content-Type="text/html"')
chrome_options.add_argument('chartset=utf-8')
#driver = webdriver.Chrome(executable_path=chromedriver_location, chrome_options=chrome_options)

def __init__():
    driver = webdriver.Chrome(executable_path=chromedriver_location, chrome_options=chrome_options)

arr=[]
"""def get_private():
    #driver = webdriver.Chrome(executable_path=chromedriver_location, chrome_options=chrome_options)
    driver.get('https://adultchat.chat-avenue.com/')
    time.sleep(5)

    try:
        users = driver.find_elements_by_xpath('//div[@class="avtrig user_item "]')
        for user in users:
            try:
                imgs = user.find_elements_by_xpath('//img')
                for img in imgs:
                    try:
                        if 'system/location/flag/GB.png' in img.get_attribute('src'):
                            arr.append(user)
                    except Exception as e:
                        pass
            except Exception as e:
                pass
    except Exception as e:
        print(e)
    #print(arr)
def send_private(message, link, message_img, a):
    #driver = webdriver.Chrome(executable_path=chromedriver_location, chrome_options=chrome_options)
    time.sleep(1)
    a.click()
    time.sleep(1)
    driver.find_element_by_xpath('//div[@class="avset avitem gprivate"]').click()
    time.sleep(2)
    #send message
    try:
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
        print('PM message sent!')
        time.sleep(2)
        #if driver.find_element_by_xpath('//span[@class="pm_notify private_count bnotify"]').is_displayed():
        time.sleep(1)
    except Exception as e:
        print(e)"""

i = 0
def login(username, password, text, pathimg, message, message_img, link):
    driver = webdriver.Chrome(executable_path=chromedriver_location, chrome_options=chrome_options)
    i=0
    
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
        #get_private()

        ##############################
        #Get private
        """driver.get('https://adultchat.chat-avenue.com/')
        time.sleep(5)

        try:
            users = driver.find_elements_by_xpath('//div[@class="avtrig user_item "]')
            for user in users:
                try:
                    imgs = user.find_elements_by_xpath('//img')
                    for img in imgs:
                        try:
                            if 'system/location/flag/GB.png' in img.get_attribute('src'):
                                arr.append(user)
                        except Exception as e:
                            pass
                except Exception as e:
                    pass
        except Exception as e:
            print(e)"""
        ##############################
        """#Send private
        time.sleep(3)
        driver.get('https://adultchat.chat-avenue.com/')
        time.sleep(7)
        arr[i].click()
        time.sleep(1)
        driver.find_element_by_xpath('//div[@class="avset avitem gprivate"]').click()
        time.sleep(2)
        #send message
        try:
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
            print('PM message sent!')
            time.sleep(2)
            #if driver.find_element_by_xpath('//span[@class="pm_notify private_count bnotify"]').is_displayed():
            time.sleep(1)
        except Exception as e:
            print(e)"""
        ##############################
        i+=1

        while True:
            try:
                driver.find_element_by_xpath('//div[@id="get_private"]').click()
                time.sleep(2)
                #if driver.find_element_by_xpath('//span[@class="pm_notify private_count bnotify"]').is_displayed():
                dms = driver.find_elements_by_xpath('//div[@class="ulist_name gprivate"]')#.click()
                time.sleep(1)
                for dm in dms:
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
                    print('Message sent!')
                    driver.find_element_by_xpath('//div[@id="get_private"]').click()
                    time.sleep(2)
                    #if driver.find_element_by_xpath('//span[@class="pm_notify private_count bnotify"]').is_displayed():
                    dms = driver.find_elements_by_xpath('//div[@class="ulist_name gprivate"]')#.click()
                    time.sleep(1)
            except Exception as e:
                print(e)

            try:
                i+=1
                #send_private(message, link, message_img, arr[i])
            except Exception as e:
                print(e)
                
            #send public message
            driver.get('https://adultchat.chat-avenue.com/')
            time.sleep(5)
            driver.find_element_by_xpath('//input[@name="content"]').send_keys(text)
            driver.find_element_by_xpath('//button[@class="default_btn csend"]').click()
            time.sleep(2)
            print('Public message!')
    except Exception as e:
        print(e)
    
    driver.close()

#login('jasamdaklemisli', 'Vojko123', 'Anyone for sexting', 'chatbot-data.png', 'Seyting?', 'logo.png', 'stafty.com')