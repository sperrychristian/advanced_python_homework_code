# We will use Linux big time in this course! 
import numpy as np 
# Classes and Objects 

# the class is the blueprint and the object is what we end up creating with the blueprint - this is the major difference between a class and an object

# using a dictionary to help set up what an object and class are 

person = {}
person['name'] = 'christian'
person['age'] = 27
person['spouse'] = 'madi'
person['grades'] = [101, 99, 98]

# dictionaries DO NOT ALLOW US TO ADD A FUNCTION - so person['avgGrade'] = def avgGrade() would not work. This is where classes and objects are useful!! 

# The following is how we are able to create a class. (we give a capitalized first letter to classes)
class C_person():
    def __init__(self, name, age, spouse, grades): # this is a standard function all classes have in order to put data in them. This init function is also known as a constructor just like the constructor of a house using a blueprint
        self.name = name
        self.age = age
        self.spouse = spouse
        self.grades = grades

        # one of the advantages of using a class is the ability to put functions inside of it
        def calcAvgGrade(self):
            return np.mean(self.grades) # this will automatically return the avg grade!
        
        # getter functions defined inside of the class, very simple function just returning the value in the object
        # getters just return the value 
        def getName():
            return self.name
        
        def getSpouse():
            return self.spouse
        
        # setter functions also go within the object 
        # setters set a new value
        def setName(self, name):
            self.name = name 

        def setSpouse(self, spouse):
            self.spouse = spouse

        def setGrades(self, grades):
            self.grades = grades
        

# the above class is our blueprint, we can now use it! 

p1 = C_person('christian', 27, 'madi', [101, 99, 98])
# p1 is a new variable or in our analogy the house we are creating - setting it = to the class is utilizing the blueprint we had previously created 

# we can access the data inside using the . operator 
print(p1.getName())
print(p1.getSpouse())
print(p1.calcAvgGrade()) 
# we can use our previously created functions to call them and set new grades! 
p1.setGrades([100, 100, 100])


# classes are most helpful when we want to utilize it over and over again, we could easily create hundreds of people using this class 

# THE MEGA ADVANTAGE OF CLASSES IS COMBINING DATA AND FUNCTIONALITY TO HAVE THE DATA AND FUNCTIONS WORK TOGETHER FOR ONE PURPOSE 

# Classes Getters & Setters
# It's much better practice for us to use getters and setters to extract data from a function rather than using print statements afterwards. We do this in the form of functions. Same goes for setters!

# IT'S BEST STYLE TO USE GETTERS AND SETTERS! 

# PRIVATIZING DATA IS KNOWN SPECIFICALLY AS ENCAPSULATION
# We want to control our class, and control how and when the class is used. 
# Us as developers have that control. 
# We do this by adding two underscores, see example below. 

# created a new class for our example
class Dog():
    def __init__(self, name, age, weight, breed, training_score, address, ssn):

        self.name = name
        self.age = age
        self.weight = weight
        self.breed = breed
        self.training_score = training_score

        # note the two underscores for dog address
        self.__address = address # the __ indicates that the variable is private and the only way it can be accessed is through using a getter and setter!  
        self.__ssn = ssn # social security number for dogs lol

        # adding getter and setter for our two private portions of the class 
        # the only way we can access private data is when working inside of the class 
        def setAddress(self, address):
            self.__address = address

        def setSSN(self, ssn):
            self.__ssn = ssn

        def getAddress(self, address):
            return self.address
        
        def getSSN(self, ssn):
            return self.ssn 

# the below function is utilizing numpy as np
    def calcAvgTrainingScore(self):
        return np.mean(self.training_score)

# creating our object from the class 
d1 = Dog('Teton', 2, 65, 'Golden Retriever', [120, 300, 5], 'doggy lane 890', 2342523423)

print(d1.getSSN()) # this is the only way to access it since the ssn is private 

# THIS WILL NOT WORK because self.__ssn is private 
print(d1.__ssn)


        


