"""
TODO: 
once I have the physical ESP32 and displays, I will be able to
write and test code much more easily. also, since I need to fill
5 hours in build week, I've decided that I'll save the bulk of the
code writing till then. I've written a basic shell for the program
here.
"""

import network
import time
import ntptime

class DigitalClock:
    def __init__(self):
        self.speed = 0.2
        self.updating = [ False ] * 6
        self.previous = ""
    def update(self, current):
        # TODO: update / display code for clock faces
        pass

class AnalogClock:
    def __init__(self):
        self.previous = ""
    def update(self, current):
        # TODO: update / display code for clock faces
        pass

class Shader:
    def __init__(self):
        self.previous = ""
    def update(self, current):
        # TODO: update / display code for clock faces
        pass

ssid = '****'
password = '********'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

print('Connecting to Wi-Fi...', end = '')
while not wlan.isconnected():
    print('.', end = '')
    time.sleep(0.5)
    
print('\nConnected! Network config:', wlan.ifconfig())

ntptime.settime()

# TODO: add more controllers
controllers = [ DigitalClock, AnalogClock, Shader ]

delay = 0.1

controller = controllers[0]()

previous = ""

done = False
while not done:
    now = time.localtime()

    formatted = "{:02d}{:02d}{:02d}".format(now[3], now[4], now[5])

    controller.update(formatted)

    previous = formatted
    time.sleep(delay)