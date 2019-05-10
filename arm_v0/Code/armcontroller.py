# -*- coding: utf-8 -*-
"""
Code to key log and send commands to raspberry pi robot arm
Created on Mon May  6 21:13:08 2019

@author: swedd
"""

import socket

UDP_IP_ADDRESS = "192.168.0.20"
UDP_PORT_NO = 6789
Message = "Hello, Server"
print("test")

clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk
def key(event):
    """shows key or tk code for the key"""
    if event.keysym == 'Escape':
        root.destroy()
    if (event.keysym == 'Right' or event.keysym == 'Left'
        or event.keysym == 'Up' or event.keysym == 'Down'):
        #send right command
        clientSock.sendto(event.keysym, (UDP_IP_ADDRESS, UDP_PORT_NO))
    if event.char == event.keysym:
        # normal number and letter characters
        print( 'Normal Key %r' % event.char )
    elif len(event.char) == 1:
        # charcters like []/.,><#$ also Return and ctrl/key
        print( 'Punctuation Key %r (%r)' % (event.keysym, event.char) )
    else:
        # f1 to f12, shift keys, caps lock, Home, End, Delete ...
        print( 'Special Key %r' % event.keysym )
root = tk.Tk()
print( "Press a key (Escape key to exit):" )
root.bind_all('<Key>', key)
# don't show the tk window
root.withdraw()
root.mainloop()