"Variables"
# Instance Var 
# Static variable / class variable
# local variable

"Instance var = var that change its value as per object is called instance var" 
# Example of Inst var
class Student:
    def __init__(self,name,rol):
        self.x=name
        self.y=rol
obj=Student('Vijay',23)
print(obj.x)
print(obj.y)


# Note : Any variable that a=has been initiliazed aside of self is identity of instance var

' Where can be instance variable declared. '
' Method where first parameter is defined as self parameter. '

# DECLARATION OF INSTANCE VARIABLE 
' Inside class and Outside class '  
'1. Inside class (self.<variable_name>) '
'2. Outside class (object.<variable_name>) '
