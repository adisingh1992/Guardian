import RPi.GPIO as gpio
from time import sleep
import os, random

#Setting GPIO-mode as BOARD for easy gpio naming
gpio.setmode(gpio.BOARD)

#Matrix pointing to different gpio pins
matrix = [ [11, 12, 13, 91],
           [15, 16, 18, 92],
           [22, 40, 93, 94],
           [95, 96, 97, 98] ]

#Matrix values used to maintain status of individual pins,
#so it does not clash with the webserver values
mat_status = [ [0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0] ]

#List, pointing to gpio pins of the relays
relay = [11, 12, 13, 15, 16, 18, 22, 40]
row = [38, 37, 36, 35]
col = [33, 31, 29, 32]

volume = -1000
all_in_check = 0

#Setting up gpio pins
for k in range(8):
    gpio.setup(relay[k], gpio.OUT)

#Keypad setup
#Columns keys values set as output pins
for i in range(4):
    gpio.setup(col[i], gpio.OUT)
    gpio.output(col[i], 1)

#Rows keys values set as input pins with pull_down resisters(inbuilt)
for j in range(4):
    gpio.setup(row[j], gpio.IN, pull_up_down = gpio.PUD_UP)

#Function activating all the relays
def all_in():
    global all_in_check
    if all_in_check == 0:
        for i in range(8):
            gpio.output(relay[i], 1)
        all_in_check = 1

#Function disabling all the relays
def all_out():
    global all_in_check
    for i in range(8):
        gpio.output(relay[i], 0)
    all_in_check = 0

#Function starting the jukebox(music player)
def jukebox_on():
    random_mp3 = random.choice(os.listdir("/var/www/html/music-library/"))
    file = " /var/www/html/music-library/"+random_mp3
    os.system('omxplayer --vol '+str(volume)+''+file+' &')
    return

#Function stopping the jukebox
def jukebox_off():
    proc = "omxplayer"
    os.system('pkill '+proc)
    volume = -1000
    return

try:
    while(True):
        sleep(.5)
        for i in range(4):
            gpio.output(col[i], 0)
            for j in range(4):
                if gpio.input(row[j])== 0:
                    pin_down = matrix[j][i]
                    if pin_down == 91:
                        jukebox_off()
                        jukebox_on()
                    elif pin_down == 92:
                        jukebox_off()
                    elif pin_down == 93:
                        pass
                    elif pin_down == 94:
                        if volume <= 0:
                            volume = volume + 200
                    elif pin_down == 95:
                        all_in()
                    elif pin_down == 96:
                        pass
                    elif pin_down == 97:
                        all_out()
                    elif pin_down == 98:
                        if volume >= 2000:
                            volume = volume - 200
                    else:  
                        if mat_status[j][i] == 0:
                            gpio.output(pin_down, 1)
                            mat_status[j][i] = 1
                        elif mat_status[j][i] == 1:
                            gpio.output(pin_down, 0)
                            mat_status[j][i] = 0
            gpio.output(col[i], 1)
except KeyboardInterrupt:
    pass
