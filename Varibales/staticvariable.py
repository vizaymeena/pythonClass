'Static variable'
# Variable that does not change its value with the change in object are static variable and can be declared inside and outside of the class

'Declare and call = inside and outside class'
'call where where inside class??'


class Student:
    'Details'
    # Static variable
    schname='Gyan Valley'
    city='bhopal'
    count=0

    # Constructor
    def __init__(self,name,city):
        self.x=name
        self.y=city
        # declaring class varable inside constructor
        Student.scode=124      
        Student.count=Student.count+1 

    # Affiliated Number
    def new(self):
        # Declaring static variable insidie instance method
        Student.schAffNum=0000

    # Print 
    def show(self):
        print(Student.schname,Student.schAffNum,Student.subject)
    
Student.subject='Commerce'    
x = Student('vijay','bhopal')
x.new()
x.show()
print(Student.count)     # count = 1

# Referencing count variable and incrementing it with number of objects created  
x2=Student('rahul',42)
print(Student.count)     # count = 2
 

