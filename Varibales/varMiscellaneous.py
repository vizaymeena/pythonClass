a ='This is local variable a '

class Gyan:
    # static var 
    schoolname='Gyan Valley'
    affNum=1234
    'Details'
    
    def __init__(self,name,qual,section):
        self.nam=name
        self.qual=qual
        self.sec=section

    def addNew(self,city):
        Gyan.city=city
    
    def show(self):
        # Instance var prints 
        print('Instance Variable below')
        print(self.nam , self.qual,self.sec)

        # Static var prints
        print('Static Variable below')
        print(Gyan.schoolname,Gyan.affNum)


obj = Gyan('Trivubhan Mishra','CA TOPPER','Corporate Section')
obj.addNew('Series')
obj.show()

# local var prints
print(a)


# Note : variable that are associated with self parameter are instance variable and can be access thoroughout the class after constructor. 