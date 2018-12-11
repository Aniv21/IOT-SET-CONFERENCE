import time
import serial
import urllib2
ser = serial.Serial('COM10', 9600)
while True:
    message = ser.readline()
    print(message)
    #print(message[19:21])
    response = urllib2.urlopen('https://api.thingspeak.com/update?api_key=EB4LSUL528VND0QQ&field1='+message[19:21])
    html = response.read()
    time.sleep(0.5)
