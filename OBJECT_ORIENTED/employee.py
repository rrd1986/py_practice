class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)

   def __del__(self):
      class_name = self.__class__.__name__
      print (class_name, "destroyed")


'''
#This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
#This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print ("Total Employee %d" % Employee.empCount)

print("-----------------------")
print (hasattr(emp1, 'salary'))    # Returns true if 'salary' attribute exists
print (getattr(emp1, 'salary'))    # Returns value of 'salary' attribute
print (setattr(emp1, 'salary', 7000))
print (getattr(emp1, 'salary')) # Set attribute 'salary' at 7000
print (delattr(emp1, 'salary'))
#print (getattr(emp1, 'salary'))   # Delete attribute 'salary'

print("-----------------------")
print ("Employee.__doc__:", Employee.__doc__)
print ("Employee.__name__:", Employee.__name__)
print ("Employee.__module__:", Employee.__module__)
print ("Employee.__bases__:", Employee.__bases__)
print ("Employee.__dict__:", Employee.__dict__ )
'''