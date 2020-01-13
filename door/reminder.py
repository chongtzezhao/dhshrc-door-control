import telepot
from time import sleep
from datetime import datetime as dt

token = '1065181249:AAFZu_58l-xJtjzoSKTK7arLeo2k0NynbxA'
bot = telepot.Bot(token)

while True:
    sleep(1)
    if dt.now().minute==23:
        bot.sendMessage(910250337, "HI")
        
