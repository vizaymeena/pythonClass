# Constructor = is a special type of method that called automatically when object created(means using parenthesis).
# Self = is a reference variable that holds address of current object of current class.
# yes we can write multiple constructor but the drawback is that python support it but there is no use of making multiple constuctor as in multiple cosntructor only the last one gets called


# Example
class Student:
    "student details"
    name="vizay"
    qual="MBA"

# using dir
print(dir(Student.__doc__))    # shows list of magic methods of dir. 
print(Student.__doc__)         # shows doc string of a class
print(Student)                 # <class '__main__.Student'>
cLs = Student
print(cLs)                     # <class '__main__.Student'>


# Parenthesis makes the class into object , wihtout () making class object is not possible
# With the help of () we are calling constructor
obj = Student()                # <__main__.Student object at 0x0000022A97936A50>
print(obj)


print(Student.__init__)         # <slot wrapper '__init__' of 'object' objects>


# Example
class Vijay:
    'Vizay Details'
    def __init__(self):
        print("Success")
        print("self:",id(self))     # Id output same at line 34

# obj2 = Vijay         
# print(obj2)
obj2 = Vijay()     
print(id(obj2))           # Id output same at line 28



# Example 
class Student2:
    def __init__(self):
        "Marksheet"
        self.name="vijay"
        self.age=23
        self.sch="Gyan Valley"
        # accesseing through self object parameter
        print(self.sch)
        print(self.age)
        print(self.name)

obj3 = Student2()
# assessing through obj3 object parameter
print(obj3.name)          
print(obj3.age)  
print(obj3.sch)  



# Example
# Putting Values dynamically inside class
class Student2:
    def __init__(self,name,rol,marks):
        "Marksheet"
        self.name=name
        self.r=rol
        self.m=marks
        # accesseing through self object parameter
        print(self.name)
        print(self.r)
        print(self.m)

obj3 = Student2("Vijay",2,23)
# assessing through obj3 object parameter
print(obj3.name)          
print(obj3.r)  
print(obj3.m)  




# Example Of multiple constructor

class Student4:
    "Constructor"
    def __init__(self,name,age,rol):
        self.x=name
        self.y=rol
        self.z=age

    def __init__(self):
        print("Not first but , Second construcutor gets called ")
    
obj4=Student4()
# Note = when the construcotr gets overloaded last of construcutor in the heirarchy gets called
# in this case the constructor at line 93 is called as it is of the last  

obj4.__init__()  # calling constructor at globally, yes it is possible
