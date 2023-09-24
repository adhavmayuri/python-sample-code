from abc import ABC
class llgm(ABC): #abstract classdef calculate_area(self): #abstract methodpass
    pass

class Square(llgm):
  length = 5
  def Area(self):
    return self.length * self.length 

class Circle(llgm):
  radius =4 
  def Area(self):
    return 3.14 * self.radius * self.radius


sq = Square() #object created for the class ‘Square’
cir = Circle() #object created for the class ‘Circle’

print("Area of a Square:", sq.Area()) #call to ‘calculate_area’ method defined inside the class ‘Square’
print("Area of a circle:", cir.Area())