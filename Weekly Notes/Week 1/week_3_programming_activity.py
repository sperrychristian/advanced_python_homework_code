# 1. Create a Student class with a init function that initializes the following variables: a_number (private), first_name, last_name, major, gpa, num_credits_enrolled

class Student:
    def __init__(self, a_number, first_name, last_name, major, gpa, num_credits_enrolled):
        self.a_number = a_number
        self.first_name = first_name
        self.last_name = last_name
        self.major = major 
        self.gpa = gpa
        self.num_credits_enrolled = num_credits_enrolled

# 2. create getters and setters for all the data variables in the Student class
    def getAnumber(self):
        return self.__a_number
    def setAnumber(self, __a_number):
        self.a_number = __a_number
    
    def getFirstName(self):
        return self.first_name
    def setFirstName(self, first_name):
        self.first_name = first_name
    
    def getLastName(self):
        return self.last_name
    def setLastName(self, last_name):
        self.last_name = last_name
    
    def getMajor(self):
        return self.major 
    def setMajor(self, major):
        self.major = major
    
    def getGPA(self):
        return self.gpa
    def setGPA(self, gpa):
        self.gpa = gpa
    
    def getNumCreditsEnrolled(self):
        return self.num_credits_enrolled
    def setNumCreditsEnrolled(self, num_credits_enrolled):
        self.num_credits_enrolled = num_credits_enrolled

# 3. create a function is_full_time_student(self) which returns True if the student is taking 12 or more credits
    def fullTimeStudent(self):
        if self.num_credits_enrolled >= 12:
            return True
        else:
            return False
        
# 4. Create a GradStudent class which inherits from the Student class

class GradStudent(Student):

# 5. overwrite the function is_full_time_student(self) which returns True if the student is taking 6 or more credits
    def fullTimeStudent(self):
        if self.num_credits_enrolled >= 6:
            return True
        else: 
            return False 
        
# 6. create 3 Student objects and 1 GradStudent objects.  Then add them to a list called students_5500

christian_student = Student(34342, 'Christian', 'Sperry', 'Information Systems', 4.0, 6)
madi_student = Student(243242, 'Madi', 'Sperry', 'Statistics', 3.8, 4)
nicole_student = Student(3242342, 'Nicole', 'Sperry', 'Business', '3.4', 12)
dennis_student = GradStudent(23443, 'Dennis', 'Sperry', 'Information Systems', 3.4, 7)

student_5500 = [christian_student, madi_student, nicole_student, dennis_student]

# 7. loop through the list and call the function is_full_time_student for all students in the list to determine if they are all full time students.
for student in student_5500:
    full_time_status = student.fullTimeStudent()
    print(student.first_name, student.last_name)
    print('Full Time Status:', full_time_status)
        

    
