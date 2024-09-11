#dishes
#restaurent

class dish:
    name:str
    price:int
    quandity:str
    
    def __init__(self,name,price,quandity):
        self.name=name
        self.price=price
        self.quandity=quandity
    def __str__(self):
        return self.name
class restaurent:


    def __init__(self,name,place):
        self.name=name
        self.place=place
        self.dishs=[]
        def add_fd(self,dish):
            self.dishs.append(dish)
        def list_food(self):
            for d in self.dishs:
             print(d)

biri_instance=dish("biri",55,"small") 
fry_instance=dish("fry",45,"large") 
rawai_instance=dish("rawai",35,"medium") 
restaurent_instance=restaurent("star","kolndy")
restaurent_instance.add_fd(biri_instance)
restaurent_instance.add_fd(rawai_instance)
restaurent_instance.list_fd()
restaurent_instance2=restaurent("janatha","kozhikde")
restaurent_instance2.add_food(biri_instance)
restaurent_instance2.add_food(fry_instance)
restaurent_instance2.add_food(rawai_instance)

                 


        




