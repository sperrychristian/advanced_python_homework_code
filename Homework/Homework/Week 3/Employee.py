# Medium Question  (5 points)
# Create a class called Employee with attributes name and salary. Implement a method within the class that increases the salary of the employee by a given percentage. Instantiate an object of the Employee class with name = "John" and salary = 5000, increase the salary by 10%, and print the updated salary.

# creating Employee class
class Employee():
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # setter functions 
    def setName(self, name):
        self.name = name
    
    def setSalary(self, salary):
        self.salary = salary

    # getter functions 
    def getName(self):
        return self.name
    
    def getSalary(self):
        return self.salary
    
    # function to increase employee salary by a given %
    def increaseSalary(self, percentage_increase):
        salary_increase = self.salary * (percentage_increase * .01)
        self.salary = self.salary + salary_increase
        return self.salary
    
# creating an object from the class 
e1 = Employee('John', 5000)

# increasing salary by 10% and printing it (function returns the new salary but for the sake of the assignment, I will also print it using my getSalary function below)
print(e1.increaseSalary(10))

# printing using getSalary function 
print(e1.getSalary())

# NO AI PROMPTS USED IN THIS PROBLEM 