# Two child can inherit properties of a single parent base class. 
"Example of Hierarchial Inheritance"
class HeirClass:
    def home(self):
        print("from Heirclass")

class Child1(HeirClass):
    def home1(self):
        print('Child 1 class')

class Child2(HeirClass):
    def home2(self):
        print("child 2 class")

obj0=HeirClass()
obj0.home()
obj1=Child1()
obj1.home1()

obj2=Child2()
obj2.home2()


