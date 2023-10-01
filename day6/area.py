import math
def area_circle(radius):
    return math.pi*radius**2
def area_cylinder(radius,height):
    circle_area=area_circle(radius)
    height_area=2*radius*math.pi*height
    return 2*circle_area+height_area
print("area of circle of radius 1 is",area_circle(2))
r=2
height=10
print("surface area of cylinder with radius",r)
print ('and height', height, 'is', area_cylinder(r,height))