# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 21:17:27 2018

@author: swed
"""

from math import *



def CalcCoordinates(angle, radius):
    rad = radians(angle)
    y = radius * sin(rad)
    x = radius * cos(rad)
    return x,y

def CalcCircularMovement(angle, radius):
    return radians(angle) * radius

def CalcDoubleAngle(angle1, radius1, angle2, radius2):
    x1,y1 = CalcCoordinates(angle1, radius1)
    x2,y2 = CalcCoordinates(angle2, radius2)
    return x1+x2,y1+y2

def LawOfCos(opp, side1, side2):
    top = (side1 * side1 + side2 * side2 - opp * opp)
    bottom = (2 * side1 * side2)
    return degrees(acos(top / bottom))

def ModifiedATan(x,y):
    if x == 0:
        if y > 0:
            return 90
        else:
            return -90
    angle = degrees(atan(y/x))
    if x < 0:
        if y > 0: 
            angle += 180
        else:
            angle -= 180
    return angle

def InverseDoubleAngle(x,y,radius1,radius2):
    dist = hypot(x,y)
    angle = ModifiedATan(x,y)
    #print("dist: " + str(dist) + " angle: " + str(angle))
    A = LawOfCos(radius2, dist, radius1) + angle
    x1,y1 = CalcCoordinates(A, radius1)
    #print(x1,y1)
    B = ModifiedATan(x - x1, y - y1)
    
    return x1,y1,A, B
    
#print(InverseDoubleAngle(1,-1,2,1))