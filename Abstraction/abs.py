# abc =  abstract base class 
# Mode nodule require to make abstract class 
# from abc import ABC,abstractmethod

from abc import ABC,abstractmethod

class BankApp(ABC):
    def login(self):
        print('Login...')

    def logout(self):
        print("logout..")
    
    def userdetails(self):
        print('user details...')
    
    @abstractmethod
    def database(self):
        # print('hellow')
        pass


class WebPage(BankApp):
    def new(self):
        print('Database connected...')

    def database(self):
        print('Hellow now it will run')

obj=WebPage()
obj.database()
obj.login()
obj.userdetails()
obj.logout()
