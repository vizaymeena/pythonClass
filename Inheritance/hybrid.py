# Hybrid Inheritance.

"Example of Hybrid Inheritance"
class HybClass:
    def home(self):
        print("from Heirclass")

class Child1(HybClass):
    def home(self):
        print('Child 1 class')

class Child2(HybClass):
    def home(self):
        print("child 2 class")

# MRO Will Follow Here properties of child 1 will appear on calling when having same names [ex= def home()].
class Child3(Child1,Child2):
    def new(self):
        print("Child 3 inheriting child1 and child2")

obj0=HybClass()
obj0.home()
obj1=Child1()
obj1.home()

obj2=Child2()
obj2.home()

print(Child3.__mro__) # Printing MRO Sequence.


obj3=Child3()
obj3.new()    # ch

# Inheritance interview oriented.

# singlestar[holds value in form of tuple] and doublestar[holds value in form of dict]
# Overloading (same class mai same nam ki 2 method python does not support overloading , how can variable lenght arugments  or keywordarguemnts help python to achieve this intend ) , overriding 
# super()
# note: Eval() can solve boolean expression esa kuch boolean expression ko solve krta hai = 2x+1=0 runtime input mai

