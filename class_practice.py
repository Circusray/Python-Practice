# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 15:41:21 2021

@author: w3416
"""
import math

class GeometricalShapes :
    def center_point(self):
        self.center_point = [0,0]
        print('center_point:', self.center_point)
        
 

class Rectangle(GeometricalShapes):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def getArea(self):
        area = self.length * self.width
        print('==getRectangleArea==')
        print('Area:', area )
      
class Circle(GeometricalShapes):
    def __init__(self, r):
        self.r = r

    def getArea(self):
        area = round(self.r ** 2 * math.pi, 2)
        print('==getCircleArea==')
        print('Area:', area )     


if __name__ == "__main__":
    myRectangle = Rectangle(3,5)
    myRectangle.getArea()
    myRectangle.center_point()
    
    myCircle = Circle(3)
    myCircle.getArea()
    myCircle.center_point()