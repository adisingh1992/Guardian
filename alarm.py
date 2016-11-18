import os, random
import RPi.GPIO as gpio
from time import sleep

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(13, gpio.OUT)
gpio.output(13, 1)

alarm_music = random.choice(os.listdir("/var/www/html/music-library/"))
file = " /var/www/html/music-library/"+alarm_music
os.system('omxplayer --vol -500 '+file+' &')
sleep(120)
os.system('pkill omxplayer')

gpio.output(13, 0)
