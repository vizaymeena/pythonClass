"insatnce Variable"
class Student:
   
    def __init__(self,name,roll,marks):
        # inside variable declared at constructor
        self.x=name
        self.y=roll
        self.z=marks
    

    def add_new(self,city):
        # instance variable declared inside instance method
        self.p=city

    def show(self):
        # instance variable call inside instance method
        print(self.x,self.y,self.z,self.p,self.sch_name)

#  instance variable Declared outside of the class.
object1=Student('vijay',101,33)
object1.sch_name='Gyan Valley Co-Ed School'
object1.add_new('bhopal')

object1.show()
        