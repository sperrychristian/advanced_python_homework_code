# Easy Question: (3 points)
# Create a class called Rectangle with attributes length and width. Implement a method within the class to calculate the area of the rectangle. Instantiate an object of the Rectangle class with length = 5 and width = 3, and print its area.

# creating rectangle class 
class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    # setter functions 
    def setLength(self, length):
        self.length = length

    def setWidth(self, width):
        self.width = width 

    # getter functions 
    def getLength(self):
        return self.length
        
    def getWidth(self):
        return self.width
        
    # function to calculate area of rectangle in class 
    def calcArea(self):
        area = self.width * self.length
        return area
        
# creating an object from the class
r1 = Rectangle(5,3)

# printing the area
print(r1.calcArea())

# NO AI PROMPTS USED IN THIS PROBLEM 