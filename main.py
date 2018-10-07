import time
import urequests
import utime
import dht
import machine

d = dht.DHT22(machine.Pin(16))
adc = machine.ADC(0)
period = 30
id = 304050
headers = {'Content-Type': 'application/json', 'Accept': 'text/plain'}



urequests.get(deviceRegisterUrl, headers=headers)

def post_data(temperature, humidity, light, cleanTime):
    data = {"deviceName":"esp8266_sensor_platform","temperature":temperature, "humidity":humidity, "light":light, "timestamp":cleanTime}
    response = urequests.post(kafkaUrl, headers=headers, json=data)
    print(response.text)
    response.close()

while True:
    time.sleep(period)
    year = utime.localtime()[0]
    month = utime.localtime()[1]
    day = utime.localtime()[2]
    hour = utime.localtime()[3]
    minute = utime.localtime()[4]
    second = utime.localtime()[5]

    cleanTime = "%s-%s-%sT%s:%s:%s" % (year, month, day, hour, minute, second)
    d.measure()
    time.sleep(2)
    temperature = d.temperature()
    humidity = d.humidity()
    light = adc.read()
    post_data(temperature, humidity, light, cleanTime)