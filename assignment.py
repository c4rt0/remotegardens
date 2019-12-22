#!/usr/bin/env python
from time import sleep

# i2c initialisation 
from smbus2 import SMBusWrapper
import struct
address = 0x08 # address on Raspberry Pi bus received with : sudo i2cdetect -y 1
 
# getting the main GPIO library
import RPi.GPIO as GPIO 


#relay initialisation
# setting a current mode
GPIO.setmode(GPIO.BCM)
#removing the warings 
GPIO.setwarnings(False)
#creating a list (array) with the number of GPIO's that I use (only two out of four are active 
# since I only plan on connecting two peristaltic pumps)
pins = [15,14] 

#dht11 initialisation (11,4) 11 is a type of a DHT sensor, 4 is a pin to where it's connected
import Adafruit_DHT
humidity, temperature = Adafruit_DHT.read_retry(11, 4)
#setting the mode for all pins so all will be switched on 
GPIO.setup(pins, GPIO.OUT)

# wia init
from wia import Wia
wia = Wia()
try: 
  wia.access_token = "My_private_Wia_key"
except:
  print("wia authorization failed\n")

# Giving the I2C device time to settle
sleep(1)

def get_float(data,index):
    bytes = bytearray(data[4*index:(index+1)*4])
    return struct.unpack("f",bytes)[0]

if __name__ == '__main__':
	while 1:
	    try:
		with SMBusWrapper(1) as bus:
		    phvalue = bus.read_i2c_block_data(address, 0, 16)
		    phvalue = get_float(phvalue,0)	   
		    print("ph: %f " % phvalue)
		    
	    except:
		print("**error**\n**")
	        continue
	    
	    # Decreasing delay may create more transmission errors.
	    sleep(0.0005)
	    if phvalue > 4:
		    for pin in reversed(pins) :
			#setting the GPIO to HIGH or 1 or true
			GPIO.output(pin,  GPIO.HIGH)
			#wait 0,5 second
			sleep(0.5)
			#setting the GPIO to LOW or 0 or false
			GPIO.output(pin,  GPIO.LOW)
			#wait 0,5 second
			sleep(0.5)

			#Checking if the current relay is running and printing it 
			if not GPIO.input(pin) : 
				print("Pin "+str(pin)+" is working")

	    print("Temp: %d C" % temperature)
            print("Humidity: %d %%" % humidity +"\n")
	    wia.Event.publish(name="temperature", data=temperature)
	    wia.Event.publish(name="ph", data=phvalue)
#cleaning all GPIO's 
GPIO.cleanup()

