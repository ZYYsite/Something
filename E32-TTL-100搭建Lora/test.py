#!/usr/bin/python
# -*- coding:utf-8 -*-
import serial
import time 

ser = serial.Serial("/dev/ttyAMA0",9600)
def main():
    k=0
    while k<100000:
        ser.write(str(k)+"\n")
        time.sleep(1)
        k=k+1
   
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        if ser != None:
            ser.close()