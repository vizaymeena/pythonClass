'Example of Multilevel Inheritance'
class Multiparent1:
    def Mulhome(self):
        print('Mulhome1')
class Multiparent2:
    
        def Mulhome(self):
          print('Mulhome2')

        #   left parent first 

class MulChild(Multiparent1,Multiparent2):
    def car(self):
        print("mul chiild")  

objmul=MulChild()
objmul.Mulhome()  # left most parent propority dega (Multiparent1)

'Note: MRO = Mehtod Resolution operator is responsible for left parent first '

