# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 21:48:08 2018

@author: swed
"""


HIGH = 660
LOW = 125
    
    
class ServoController:
    low_limit = LOW
    current_position = 0
    actual_position = 0.0
    high_limit = HIGH
    loop_delay = 0.05
    target = 0
    velocity = 0

    def __init__(self, position,
                 low_limit = LOW,
                 high_limit = HIGH):
        self.current_position = position
        self.actual_position = position
        self.target = position
        self.low_limit = low_limit
        self.high_limit = high_limit
        
    def move(self, target, time):
        self.target = target
        self.velocity = (target - self.current_position) / time
    
    def update(self):
        self.actual_position += (self.velocity * self.loop_delay)
        
        if self.actual_position < self.low_limit:
            self.actual_position = self.low_limit
            self.velocity = 0
            
        elif self.actual_position > self.high_limit:
            self.actual_position = self.high_limit
            self.velocity = 0
            
        roundedVal = round(self.actual_position)
        if int(roundedVal) == self.target:
            self.actual_position = self.target
            self.velocity = 0
            
        self.current_position = roundedVal
        
        