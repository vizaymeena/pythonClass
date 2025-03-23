# # Two child can inherit properties of a single parent base class. 
# "Example of Hierarchial Inheritance"
# class HeirClass:
#     def home(self):
#         print("from Heirclass")

# class Child1(HeirClass):
#     def home1(self):
#         print('Child 1 class')

# class Child2(HeirClass):
#     def home2(self):
#         print("child 2 class")

# obj0=HeirClass()
# obj0.home()
# obj1=Child1()
# obj1.home1()

# obj2=Child2()
# obj2.home2()

# Two child can inherit properties of a single parent base class. 
"Example of Hierarchial Inheritance"
class HeirClass:
    def home(self):
        print("from Heirclass")

class Child1(HeirClass):
    def home(self):
        print('Child 1 class')
        super().home()
        # This way is not considered as inhertiance thats called a direct call of a different class.
        # HeirClass.Home(self)

class Child2(HeirClass):
    def home(self):
        print("child 2 class")

obj0=HeirClass()

# if super method is not used then the home function of self contain within child class will execute.
obj1=Child1()
obj1.home() # home called of parent class through child class

obj2=Child2()




