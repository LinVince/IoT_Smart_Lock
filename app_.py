#Run on PC

import socket
import tkinter as tk
import re
import tkinter as tk
from tkinter import *
from tkinter import Text
import PIL
from PIL import ImageTk, Image
import os
import codecs
import sys
from tkinter.font import Font


HOST = '192.168.137.246'  # The server's hostname or IP address
PORT = 12345        # The port used by the server


s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

def auth():
    global s
    s.sendall(b'auth')
    data = s.recv(1024)
    data=data.decode('utf-8')
    t.insert(END, data)    
    print('Received', repr(data))

def lock():
    global s
    s.sendall(b'lock')
    data = s.recv(1024)
    t.insert(END, data) 
    print('Received', repr(data))

def unlock():
    global s
    s.sendall(b'unlock')
    data = s.recv(1024)
    t.insert(END, data) 
    print('Received', repr(data))

def reset():
    global s
    s.sendall(b'reset')
    data = s.recv(1024)
    t.insert(END, data) 
    print('Received', repr(data))




win=tk.Tk()
win.title('IKV')
win.geometry('1500x500')
win.resizable(width='1500', height='1000')



#iconImage=tk.PhotoImage(master=win, data=icon)
#tk.Label(image=iconImage).pack(side=LEFT)



label2=tk.Label(win, text='\nCopyright © 2019 InfoKeyVault Technology. All rights reserved. ', wraplength='1000',justify='left',)
label2.pack(side=BOTTOM)



#label=tk.Label(win, text='\n',wraplength='1000',justify='center',)
#label.pack()
label4=tk.Label(win, text="",wraplength='1000',justify='left')
label4.pack(side=TOP)
#ent=tk.Entry(win,width=100)
#ent.pack(side=TOP)
#label0=tk.Label(win, text="\nChoose a mode. If chosen wrongly, it won't run.\n",wraplength='1000',justify='left')
#label0.pack()
frame1=tk.Frame(win,width=20)
frame2=tk.Frame(win,width=40)
frame2.pack(anchor=N)
frame1.pack(anchor=N)

#ent=tk.Entry(frame2,width=115)
#ent.pack(side=LEFT)

#label1=tk.Label(frame1,text='Authentication  ')
#label2=tk.Label(frame1,text='Lock')
#label3=tk.Label(frame1,text='Wikipedia')
#label5=tk.Label(frame1,text='Quizlet')
button=tk.Button(frame1,text='Auth',command=auth)
button2=tk.Button(frame1,text='Lock',command=lock)
button3=tk.Button(frame1,text='Unlock',command=unlock)
button4=tk.Button(frame1,text='Reset',command=reset)
#button6=tk.Button(frame1,text='Eng - Eng',command=WK_EE)
#button7=tk.Button(frame1,text='Eng - Ch',command=WK_EC)
#button4=tk.Button(win,text='Delete',command=DET)
#button5=tk.Button(frame2,text='Delete',command=DEE)
#button8=tk.Button(frame1,text='Eng - Eng',command=QEE)
#button9=tk.Button(frame1,text='Eng - Ch',command=QEC)
#label1.pack(side=LEFT)
#button5.pack(side=LEFT,padx=5)
button.pack(side=LEFT)
#label2.pack(side=LEFT,padx=10)
button2.pack(side=LEFT)
button3.pack(side=LEFT,padx=0)
button4.pack(side=BOTTOM,fill=X)
#label3.pack(side=LEFT,padx=10)
#button6.pack(side=LEFT,padx=0)
#button7.pack(side=LEFT)
#label5.pack(side=LEFT,padx=10)
#button8.pack(side=LEFT)
#button9.pack(side=LEFT)


myFont =Font(family="Calibri Light", size=14)
t=Text(win, height=50, width=350)
#s=Scrollbar(win)
#s.pack(side=RIGHT, fill=Y)
t.pack(side=RIGHT)
#s.config(command=t.yview)
#t.config(yscrollcommand=s.set)
t.configure(font=myFont)

win.mainloop()
