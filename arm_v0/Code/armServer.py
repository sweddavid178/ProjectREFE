# -*- coding: utf-8 -*-
"""
Created on Mon May  6 21:30:43 2019

@author: swedd
"""

# Again we import the necessary socket python module
import socket

from servoControl import *
import threading
import time
# Import the PCA9685 module.
import Adafruit_PCA9685

# Here we define the UDP IP address as well as the port number that we have
# already defined in the client python script.
UDP_IP_ADDRESS = "192.168.0.20"
UDP_PORT_NO = 6789
# declare our serverSocket upon which
# we will be listening for UDP messages
serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# One difference is that we will have to bind our declared IP address
# and port number to our newly declared serverSock
serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))
serverSock.settimeout(0.1)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)

knee = ServoController(393)
hip = ServoController(393)
controlState = 0;

def update_pwm(delay, run_event):
    global knee
    while run_event.is_set():
        time.sleep(delay)
        knee.update()
        hip.update()
        pwm.set_pwm(1, 0, int(knee.current_position))
        pwm.set_pwm(0, 0, int(hip.current_position))
        print(knee.current_position)
        
def server_thread(delay, run_event):
    global controlState
    while run_event.is_set():
        time.sleep(delay)
        try:
            data, addr = serverSock.recvfrom(1024)
            print("Message: ", data)
            if data == "Right":
                controlState = 1;
            elif data == "Left":
                controlState = 2;
            elif data == "Up":
                controlState = 3;
            elif data == "Down":
                controlState = 4;
            else:
                controlState = 0
        except socket.timeout:
            controlState = 0
            print("timeout")

def main():
    global knee
    run_event = threading.Event()
    run_event.set()
    t1 = threading.Thread(target = update_pwm, args = (0.05, run_event))
    t1.daemon = True
    run_event2 = threading.Event()
    run_event2.set()
    t2 = threading.Thread(target = server_thread, args = (0.05, run_event2))
    t2.daemon = True
    #thread.start_new_thread(update, 0.017)
    
    try:
        t1.start()
        t2.start()
        while 1:
            if controlState == 1:
                knee.move(knee.current_position + 10, 0.05)
            elif controlState == 2:
                knee.move(knee.current_position - 10, 0.05)
            elif controlState == 3:
                hip.move(hip.current_position + 10, 0.05)
            elif controlState == 4:
                hip.move(hip.current_position - 10, 0.05)
            time.sleep(0.1)
    except KeyboardInterrupt:
        print( "attempting to close threads")
        run_event.clear()
        run_event2.clear()
        t1.join()
        t2.join()
        print ("threads successfully closed")

if __name__ == '__main__':
    main()





