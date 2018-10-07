import network
import webrepl
from ntptime import settime

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
    print('connecting to network...')
    wlan.connect('ARRIS-XX', 'XX')
    while not wlan.isconnected():
        pass
print('network config:', wlan.ifconfig())

webrepl.start()
settime()