#import builtins

#for name in builtins.__doc__:
#    print (name)
#print (abs(-155))


#class Student:
#    pass

#class Marks:
#    pass

#student1 = Student()
#marks1 = Marks ()
#print(isinstance(student1, Student))
#print(isinstance(marks1, Marks))
#print(issubclass(Student, object))
#print(issubclass(Marks, object))

#class Rectangle():
#    def __init__(self, length, width):
#        self.length = length
#        self.width = width
#
#    def area_rec(self):
#        return self.width*self.length
#
#RectangleArea = Rectangle(10, 5)
#print(RectangleArea.area_rec())

import math
class Circle():
    def __init__(self, radius):
        self.radius = radius

    def area_circ(self):
        return (self.radius*self.radius)*math.pi

    def perim_circ(self):
        return(2*self.radius)*math.pi

CircleRad = Circle(int(input("Please insert radius value: ")))
print("The area is: ", (CircleRad.area_circ)())
print("The perimeter is: ", (CircleRad.perim_circ)())