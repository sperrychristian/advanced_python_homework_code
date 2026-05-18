# sometimes we need to add to a class, or extend a class later on. We do this using a concept called inheritance. 

# parent child relationship
# the original or first class is known as the parent 
# the class that is derived from the original class is known as a the child 

# below is an example 
class Car:
    def __init__(self, make, model, year, purchase_price, milage):
        self.malke = make
        self.model = model
        self.year = year
        self.purchase_price = purchase_price
        self.milage = milage

#  function to find the new current value 
    def currentValue(self, current_year):
        return self.purchase_price * (.90 ** (current_year - self.year))
    
sperry_truck = Car('toyota', 'tacoma', 2023, 42000, 39000)

# we can call the function held in every car class to see the current value of sperry_truck
print(sperry_truck.currentValue(2026))

# Antique cars appreciate over time instead of depreciating
# we can create an inheritated class or child class using the syntax below 
# all of the functions in the parent class are moved into the child automatically 

class AntiqueCar(Car):

    # function to handle appreciating value
    def currentValue(self, current_year):
        return self.purchase_price *(1.03 ** (current_year-self.year))
    
# creating a new object from the class and printing the value of an appreciating car to show functionality
antique_car = AntiqueCar('ford', 'mustang', 1920, 60000, 60000)

print(antique_car.currentValue(2026))

# polymorphism
# any peice of a data a parent class has, you can assume the child also has it 

sperry_car = Car('toyota', 'corolla', 2006, 15000, 15000)

# list of cars 
vehicles = [sperry_truck, sperry_truck, antique_car]

# we can now iterate through this list of objects 
total_value = 0

for vehicle in vehicles:
    total_value += vehicle.currentValue(2026)
    print(type(vehicle)) # we can print out which type of class, but our code doesn't care. It just calls the currentValue function when appropriate! 

print('total vehicle value:', total_value)
    
  # we mixed together the parent and child classes then used them together in the same list! Polymorphism!
        

