# Hard Question (7 points)

# Create a class called Pet with attributes name and age. Implement a method within the class to calculate the age of the pet in equivalent human years. Additionally, create a class variable called species to store the species of the pet. Implement a method within the class that takes the species of the pet as input and returns the average lifespan for that species.

# Instantiate three objects of the Pet class with different names, ages, and species.
# Calculate and print the age of each pet in human years.
# Use the average lifespan function to retrieve and print the average lifespan for each pet's species.

# creating pet class
class Pet():
    def __init__(self, name, age, species):
        self.name = name
        self.age = age 
        self.species = species.lower() # converting to lowercase so I can match it up with my pet dictionary later in the problem

    # setter functions 
    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age

    def setSpecies(self, species):
        self.species = species
        
    # getter functions
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
    def getSpecies(self):
        return self.species
    
    # dictionarys that hold the information I will use in my functions
    pet_to_human_years = {
    "dog": 7,
    "cat": 6,
    "rabbit": 7,
    "guinea pig": 13,
    "hamster": 30,
    "rat": 30,
    "mouse": 40,
    "gerbil": 22,
    "chinchilla": 7,
    "ferret": 10,
    "hedgehog": 16,
    "goldfish": 5,
    "betta": 18,
    "gecko": 5,
    "python": 3,
    "turtle": 2,
    "tortoise": 1,
    "horse": 3,
}
    
    pet_avg_lifespan = {
    "dog": 12,
    "cat": 15,
    "rabbit": 10,
    "guinea pig": 6,
    "hamster": 2.5,
    "rat": 2.5,
    "mouse": 2,
    "gerbil": 3.5,
    "chinchilla": 12,
    "ferret": 8,
    "hedgehog": 5,
    "goldfish": 15,
    "betta": 4,
    "gecko": 15,
    "python": 25,
    "turtle": 40,
    "tortoise": 75,
    "horse": 28,
}
    
    # function to calculate the age of the pet in human years that uses my previously defined dictionary holding human year conversions to calculate human years
    def convertToHumanYears(self):
        human_age = self.age * self.pet_to_human_years[self.species]
        return human_age

    def avgLifespan(self):
        average_lifespan = self.pet_avg_lifespan[self.species]
        return average_lifespan
    
# creating three objects from the pet class
p1 = Pet('Teton', 2, 'dog')
p2 = Pet('Bug', 5, 'horse')
p3 = Pet('Cheeselicker', 1.5, 'mouse')

# calculating and printing the age of each pet in human years
print(p1.convertToHumanYears())
print(p2.convertToHumanYears())
print(p3.convertToHumanYears())

# using the average lifespan function to retrieve and print the average lifespan for each pet's species
print(p1.avgLifespan())
print(p2.avgLifespan())
print(p3.avgLifespan())

# USED AI TO GATHER A LIST OF PETS WITH CONVERSIONS TO HUMAN YEARS AND THEIR AVG LIFESPANS