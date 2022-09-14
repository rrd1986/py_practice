from employee import Employee

class Child(Employee): # define child class
   def __init__(self):
      print ("Calling child constructor")
      super().__init__("rashmi", 50000000)

   def childMethod(self):
      print ('Calling child method')


C = Child()
C.displayCount()
print(C.empCount)
