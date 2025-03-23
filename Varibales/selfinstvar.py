class Practice:
    def __init__(self,name,place,city):
        self.na=name
        self.pl=place
        self.ci=city

    def add_info(self,age):
        self.age=age

    def show(self):
        print(self.na,self.pl,self.ci,self.age)

obj1=Practice('vijay','bagoniya','bhopal')
obj1.age=23

obj1.show()





