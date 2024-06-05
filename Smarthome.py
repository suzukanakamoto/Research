import time, datetime
import RPi.GPIO as GPIO
import telepot
from telepot.loop import MessageLoop

lpkmrmandi = 26
kipas = 19
lptamu = 13
pintu = 18

now = datetime.datetime.now()
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
 
 
#LED lpkmrmandi
GPIO.setup(lpkmrmandi, GPIO.OUT)
GPIO.output(lpkmrmandi, 0) #Off initially
#LED kipas
GPIO.setup(kipas, GPIO.OUT)
GPIO.output(kipas, 0) #Off initially
 #LED lptamu
GPIO.setup(lptamu, GPIO.OUT)
GPIO.output(lptamu, 0) #Off initially
#LED pintu
GPIO.setup(pintu, GPIO.OUT)
GPIO.output(pintu, 0) #Off initially

def action(msg):
    chat_id = msg['chat']['id']
    command = msg['text']


    if 'on' in command:
        message = "Turned on "
        if 'lpkmrmandi' in command:
            message = message + "lpkmrmandi "
            GPIO.output(lpkmrmandi, 0)
        if 'kipas' in command:
            message = message + "kipas "
            GPIO.output(kipas, 0)
        if 'lptamu' in command:
            message = message + "lptamu "
            GPIO.output(lptamu, 0)
        if 'pintu' in command:
            message = message + "pintu "
            GPIO.output(pintu, 0)
        if 'all' in command:
            message = message + "semua "
            GPIO.output(lpkmrmandi, 0)
            GPIO.output(kipas, 0)
            GPIO.output(lptamu, 0)
            GPIO.output(pintu, 0)
        message = message + "terbuka"
        telegram_bot.sendMessage (chat_id, message)

    if 'off' in command:
        message = "Turned off "
        if 'lpkmrmandi' in command:
            message = message + "lpkmrmandi "
            GPIO.output(lpkmrmandi, 1)
        if 'kipas' in command:
            message = message + "kipas "
            GPIO.output(kipas, 1)
        if 'lptamu' in command:
            message = message + "lptamu "
            GPIO.output(lptamu, 1)
        if 'pintu' in command:
            message = message + "pintu "
            GPIO.output(pintu, 1)
        if 'all' in command:
            message = message + "semua "
            GPIO.output(lpkmrmandi, 1)
            GPIO.output(kipas, 1)
            GPIO.output(lptamu, 1)
            GPIO.output(pintu, 1)
        message = message + "tertutup"
        telegram_bot.sendMessage (chat_id, message)

telegram_bot = telepot.Bot('5254086618:AAGNMz4rRTKUYx0IofVuIitUZHN8NNmIMls')
print (telegram_bot.getMe())

MessageLoop(telegram_bot, action).run_as_thread()
print ('Up and Running....')

while 1:
    time.sleep(10)

