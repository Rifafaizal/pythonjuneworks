class book:
    name=str
    author=str
    price=int
    def __init__(self,name,author,price):
        self.name=name
        self.author=author
        self.price=price
    def display_book(self):
        print(self.name,self.author,self.price)





    


        # __str__  =>string method in jS 
    def __str__(self):
        return self.name



instance_book1=book("rifa","raff",55)
    
instance_book2=book("riffafa","raff",98)
instance_book1.display_book()
print(instance_book2)




# print(book_instance2) >=ingane kodkkmbol hexadecimal value ahn print aava athin __str__ kodkknm













         

