from src.bots.making import signup, verify
from src.libs.emailverification import getaddress
from src.bots.doing import do, __init__
from src.db.database import Database
import json

def run(text, pathimg, message, message_img, link, i):
    email = getaddress()
    signup(email)
    verify('Vojko123', email)
    driver = __init__()
    do(driver, email, 'Vojko123', text, pathimg, message, message_img, link, i)

import threading

datas = open('data/data.json')
datas = json.load(datas)

i=0
for data in datas['data']:
    i+=1
    threading.Thread(target=run, args=[data['text'], data['pathimg'], data['message'], data['message_img'], data['link'], i]).start()