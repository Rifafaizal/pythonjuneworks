#overriding-implement okey allenkil



class parent:
    def bike(self):
        print("access")
    def choclate(self):
        print("kitkat") 
class child(parent):
    def choclate(self):
        print("tobleron")
    
child_instance=child()
child_instance.bike()
child_instance.choclate() 


class shop:
    def choclate(self):
        print("galaxy")
    def icecream(self):
        print("vanila")  
class product(shop):
    def choclate(self):
        print("kinder")
product_instance=product()
product_instance.choclate()
product_instance.icecream()                  
