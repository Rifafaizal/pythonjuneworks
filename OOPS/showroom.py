class bike:
    name=str
    brand=str
    price=str
    def __init__(self,name,brand,price):
        self.name=name
        self.brand=brand
        self.price=price
    def __str__(self):
        return self.name


class showroom:
    name=str
    place=str
    def __init__(self,name,place):
        self.name=name
        self.place=place
        self.bikes=[]
    def add_vehicle(self,bike):
        self.bikes.append(bike)
    def list_vehicles(self):

        for b in self.bikes:


            print(b)


hunter_instance=bike("hunter","re",200000)
activa_instance=bike("activa","hinda",100000)
dominar_instance=bike("dominar","bajaj",120000)
himalaya_instance=bike("himalaya","re",220000)

showroom_instance=showroom("popular","kakkanad")

showroom_instance.add_vehicle(hunter_instance)

showroom_instance.add_vehicle(dominar_instance)

showroom_instance.list_vehicles()

showroom_instance2=showroom("tags","thrissur")

showroom_instance2.add_vehicle(hunter_instance)
showroom_instance2.add_vehicle(activa_instance)
showroom_instance2.add_vehicle(himalaya_instance)
showroom_instance2.add_vehicle(dominar_instance)

showroom_instance2.list_vehicles()

        
        