import socket, random, time
from colorama import *
import threading
import re
from os import path
from sys import platform
import requests,webbrowser
import os

host = (Fore.RED+"""\n                  Your platform is """+ platform+Style.RESET_ALL)
print(host)
name = socket.gethostname()
myHostName = socket.gethostname()
active = requests.get('https://api.ipify.org/?format=json').json()
ip1 = active['ip']
print ("        \n                  Your iP iS "+Fore.CYAN+ip1 )

app_name = " ReSt PasS iG By             @ hxn.py << insta "
print(Fore.CYAN+'\n [ + ] Welcome you in my program' + app_name + "Made by HEXiN")
url = "https://instagram.com/hxn.py/"
webbrowser.open(url)

user = input (Fore.YELLOW+"\n\n [+] Enter user or Num or Email to reset =>> : ")

url = "https://www.instagram.com/accounts/account_recovery_send_ajax/"

headers = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'content-length': '81',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'ig_did=39B887B7-CB8C-43E7-B0D0-5BCF5C1BD61E; ig_nrcb=1; csrftoken=lziZ8vgdYVm9lZ5qwS0cCxAnCE1q8dwh; mid=YmVLWgALAAEkorDZY6V8Csqt4lm6',
    'dnt': '1',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/accounts/password/reset/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
    'x-asbd-id': '198387',
    'x-csrftoken': 'lziZ8vgdYVm9lZ5qwS0cCxAnCE1q8dwh',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': '0',
    'x-instagram-ajax': '20e2a5e214f4',
    'x-requested-with': 'XMLHttpRequest',
}

data = {
    'email_or_username': user,
    'recaptcha_challenge_field':'',
    'flow': '',
    'app_id': '',
    'source_account_id': '',
}
print(Fore.BLUE+"\n [+] Done reset is send")

requests.post(url,  headers=headers,  data=data)

url = "https://t.me/HEXiN1K/"
webbrowser.open(url)
