from src.making import signup, verify
from src.emailverification import getaddress
from src.doing import login, __init__
import os

f = open('data/vconfig.txt', 'r')
lines = f.read().split('\n')
for line in lines:
    if 'text_file' in line:
        line = line.replace('text_file=', '')
        text=line
    if 'message_text' in line:
        line = line.replace('message_text=', '')
        message=line
    if 'message_img' in line:
        line = line.replace('message_img=', '')
        message_img=line
    if 'link' in line:
        line = line.replace('link=', '')
        link=line
    if 'path_img' in line:
        line = line.replace('path_img=', '')
        pathimg=line

from multiprocessing import Process
from multiprocessing.dummy import Pool as ThreadPool

arr=[
    '1',
    '2',
    '3',
    '4',
    '5'
]

def run(arr):
    email = getaddress()
    signup(email)
    verify('Vojko123', email)
    login(email, 'Vojko123', text, pathimg, message, message_img, link)
#run(arr)

import tkinter as tk
from tkinter import *
  
root=tk.Tk()
root.title('Chat bot')
root.geometry("250x400")
name_var=tk.StringVar()
name_va=tk.StringVar()
name_v=tk.StringVar()
name_=tk.StringVar()
root.wm_iconbitmap('data/chatbot-data.ico')

num=1
def submit():
    name=name_var.get()
    name_var.set("")
    num = int(name)
    pool = ThreadPool(num)
    pool.map(run, arr)
    pool.close()
    pool.join()
name_label = tk.Label(root, text = 'Number', font=('calibre',10, 'bold'))
name_entry = tk.Entry(root,textvariable = name_var, font=('calibre',10,'normal'))

name_labe = tk.Label(root, text = 'Website', font=('calibre',10, 'bold'))
name_entr = tk.Entry(root,textvariable = name_va, font=('calibre',10,'normal'))

name_lab = tk.Label(root, text = 'Emails', font=('calibre',10, 'bold'))
name_ent = tk.Entry(root,textvariable = name_v, font=('calibre',10,'normal'))

name_lb = tk.Label(root, text = 'Seconds', font=('calibre',10, 'bold'))
name_et = tk.Entry(root,textvariable = name_, font=('calibre',10,'normal'))

sub_btn=tk.Button(root,text = 'Start', command = submit)
name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
name_labe.grid(row=2,column=0)
name_entr.grid(row=2,column=1)
name_lab.grid(row=4,column=0)
name_ent.grid(row=4,column=1)
name_lb.grid(row=6,column=0)
name_et.grid(row=6,column=1)
sub_btn.grid(row=8,column=2)
root.mainloop()
