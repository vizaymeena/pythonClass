# "Types of Inheritancce"
# # 1. Single Inheritance

# 'PARENT -----> CHILD'

# # 2. Multiple Inheritance

# ' FATHER ---- MOTHER '
 
#       'CHILD'  # inheriting properties of multi parent

# # 3. Multi-level Inheritance

# ' Grand Parent ---> Parent ----> Child '  # flow from multilevel to the chid class

# # 4. Hierarichial Inheritance
#           'Parent'

#    ' Child 1 '  ' Child 2  '
#    "a programming technique that allows multiple childern to inherit from a single parent class"



# =----------------------------------------------------------------------------------------------------------------=

'Example of Single Inheirtance'
class Parent:
    x=10
    def home(self):
        print("Parent home")

class Child(Parent):
    y=20
    def homeless(self):
        print('Child Homeless')


obj1=Parent()
obj1.home()


obj=Child()
obj.homeless()

print(obj.x) # Accessing variable of PArent class through child class using single inheritance 
print(obj.y)
# = ----------------------------------------------------------------------------------------------------------- =

# =----------------------------------------------------------------------------------------------------------------=


'Example of MultiLevel Inheritance'

class Fuel:
    x="hey this is Grand Parent"
    def Fl(self):
        print("This is dadaji")

class Price(Fuel):
    y='This is Parent'
    def Pr(self):
        print('This is pitaji')

class Consumer(Price):
    z='This is Child'

    # super method allows access to methods and properties of a parent or superclass from a child or subclass
'Note: Method overriding is supported in python'
'Note: Mehtod overloading is not supported in python'
    # super().Fl()
    def Con(self):
        print('This is betaji')

obj0=Fuel()
obj0.Fl()
print(obj0.x)    #  hey this is Grand Parent

obj1=Price()
obj1.Pr()
print(obj1.x)    #  hey this is Grand Parent

obj2=Consumer()
obj2.Con()
print(obj2.x)    #  hey this is Grand Parent 





