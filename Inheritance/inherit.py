# Parent to child accessable properties
# why use inheritance and its advantages??
# 

class A:
    x=10
    y=20
    def home(self):
        print('This is home def')

    def Car(self):
        print('Hav a car')

# Inheriting properties of A
class B(A):
    def newhome(self):
        print('new home')

obj=B()

y = obj.x
print(y)

# calling properties of a thorugh Class B() as class b inheirts properties of A
obj.home()
obj.Car()
obj.newhome()
