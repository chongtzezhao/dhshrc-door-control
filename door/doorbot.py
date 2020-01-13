import telepot
from telepot.loop import MessageLoop
from pprint import pprint
from datetime import datetime as dt
from time import sleep
import pigpio

print("bot starting...")
# CONSTANTS AND AUTHORISATION DATA

token = '1065181249:AAFZu_58l-xJtjzoSKTK7arLeo2k0NynbxA'
bot = telepot.Bot(token)

CHAT_IDS = [956428669, 68180890, 910250337]
MORNING_REMINDER = [910250337, 956428669]

COMMANDS = ["Open"]

PIN = 2
PW_MIN = 550
PW_MAX = 2250

disengaged = 1500
engaged = PW_MAX

def newDatetime():
    return str(dt.now())[:-7]

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
        
        try:
            with open("messages.txt", "a") as file:
                file.write(newDatetime() + ',' + str(chat_id) + ',' + msg['text'])
                file.write("\n")
        except:
            with open("messages.txt", "w") as file:
                file.write(newDatetime() + ',' + str(chat_id) + ',' + msg['text'])
                file.write("\n")

        cmd = msg['text'].capitalize()
        
        '''if chat_id not in CHAT_IDS:
            bot.sendMessage(chat_id, "You have not registered your telegram ID. Please message @shrcrequestbot to get added.")
            return'''

        if dt.today().weekday()>4 or dt.now().hour<7 or dt.now().hour+(dt.now().minute/60)>=6.75+12:
            bot.sendMessage(chat_id, "Room is out of bounds. Door not unlocked")
            return

        if cmd not in COMMANDS:
            bot.sendMessage(chat_id, 'Invalid command. Send "open" to unlock door')
            return
        
        io = pigpio.pi()
        io.set_servo_pulsewidth(PIN, engaged)
        sleep(0.4)
        io.set_servo_pulsewidth(PIN, disengaged)
        sleep(1)
        io.set_PWM_dutycycle(PIN, 0)
        bot.sendMessage(chat_id, 'Door successfully unlocked')

MessageLoop(bot, handle).run_as_thread()
