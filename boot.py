import network
import webrepl

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
    print('connecting to network...')
    wlan.connect('ARRIS-8422', 'HCDC3H7C7MFFWM4J')
    while not wlan.isconnected():
        pass
print('network config:', wlan.ifconfig())

webrepl.start()