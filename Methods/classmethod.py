class Book:
    price=100
    total_pages=500
    def __init__(self,title,author):
        self.title=title
        self.author=author

    @classmethod 
    def update(cls,newprice,newpagescount,author2):
        cls.newprice=newprice
        cls.totalpages=newpagescount
        cls.author2=author2

    @classmethod
    def add_new(cls,author):
        cls.author=author
    
    def showdetails(self):
        print(self.title,self.author)

obj=Book('Heroic','vijay')
obj.update(500,300,'ramsingh')
obj.showdetails()

print(obj.title)
        

