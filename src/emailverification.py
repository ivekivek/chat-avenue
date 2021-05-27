import requests
import json
from bs4 import BeautifulSoup as bs

def getaddress():
    try:
        url = 'https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1'
        res = requests.get(url)
        return res.text.replace('["', '').replace('"]', '')
    except Exception as e:
        print(e)

def getmessageid(email):
    login = email.split('@')[0]
    domain = email.split('@')[1]

    try:
        url = f'https://www.1secmail.com/api/v1/?action=getMessages&login={login}&domain={domain}'
        res = requests.get(url)
        return res.json()[0]['id']
    except Exception as e:
        print(e)

def getmessage(email):
    login = email.split('@')[0]
    domain = email.split('@')[1]

    message_id = getmessageid(email)

    try:
        url = f'https://www.1secmail.com/api/v1/?action=readMessage&login={login}&domain={domain}&id={message_id}'
        res = requests.get(url)
        return res.json()['body'].split('Verification code : ')[1].split('\t')[0]
    except Exception as e:
        print(e)