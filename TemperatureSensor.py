import os
import glob
import time
 
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
<<<<<<< HEAD

device_file = glob.glob('/sys/bus/w1/devices/' + '28*')[0] + '/w1_slave'
 


def readfile():

    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def getTemperatura():
    lines = readfile()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = readfile()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c
	
while True:
	print(getTemperatura())	
	time.sleep(1)
	
