#!/usr/bin/python
#-*-coding:utf-8 -*-
#Run on Raspberry Pi

import socket
import subprocess
from subprocess import Popen, PIPE
import time
import codecs
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(5,GPIO.OUT,initial=GPIO.LOW)

  

s=socket.socket()

host="192.168.66.169"
print(host)
port=12345
s.bind((host,port))
s.listen(5)
c,addr=s.accept()
print("Got connection from",addr)
sk='0'
message=''

while True:    
    msg=c.recv(1024)
    msg2=msg.decode('utf-8')
    print (msg2)
    if msg2 == "auth":
        s=subprocess.Popen("sudo ./tester 17", shell=True, stdout=subprocess.PIPE)
        out=s.stdout.readlines()
        sk=''
        for i in out:
            i=i.decode('utf-8')
            sk=sk+i
        #sk=codecs.decode(sk,encoding='utf-8')
        #cmd=input("What? ")
        #cmd=cmd.encode('utf-8')
        #c.sendall(cmd)
        sk=sk.encode('utf-8')
        c.sendall(sk)
        #print (msg2)
    if msg2 == "lock":
        if sk is not '0':            
            GPIO.output(5,GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(5,GPIO.LOW)
            message="Locked!!"
            message=message.encode('utf-8')
            c.sendall(message)
        elif sk == '0':            
            message="Without Authentication"
            message=message.encode('utf-8')
            c.sendall(message)
    if msg2 == "unlock":
        if sk is not '0':
            GPIO.output(3,GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(3,GPIO.LOW)
            message="Unlocked!!"
            message=message.encode('utf-8')
            c.sendall(message)
        elif sk == '0':
            message="Without Authentication"
            message=message.encode('utf-8')
            c.sendall(message)
    if msg2 == "reset":
        sk='0'
        message="Reset!"
        message=message.encode('utf-8')
        c.sendall(message)
                                   
    continue
