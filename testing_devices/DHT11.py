#!/usr/bin/python
# Original code found @ https://www.programcreek.com/python/example/92777/Adafruit_DHT.read_retry
# Here I slightly modified original version

import sys
import Adafruit_DHT

humidity, temperature = Adafruit_DHT.read_retry(11, 4)


while True: 
    print("Temp: %d C" % temperature)
    print("\nHumidity: %d %%" % humidity)
