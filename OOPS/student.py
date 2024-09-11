class student:
    name:str
    id:str
    age:int
    address:str
    contact:int
    gender:str
    # venenkil kodkka nirbandam illa.identify cheyyan kodkkam

    # initialising instants classname =>constructor
    # python=>__init__
    # java=>classname()
    # javascript=>constructor()


    def __init__(self,name,id,age,address,contact,gender):
        # set_student-instants variable ne initialise cheyyan
        # initialize
        # self:current object nte nme
        #self. varnne ellm instants variables ahn


        self.name=name   
        self.id=id
        self.age=age
        self.address=address
        self.contact=contact
        self.gender=gender
         
    def display_student(self):
        print(self.name,self.id,self.age,self.address,self.contact,self.gender)  



#creating objects


#reference_name=classname

student_instance=student("rifa","100",19,"mafas",90744174,"female") #classnme
# student_instance.set_student("rifa","100",19,"mafas",90744174,"female")=>constructor kdkkmbo ingana vnda.mele student nte ullil kodthamai
student_instance.display_student()

   




# class house:
#     name:str
#     place:str
#     def __init__(self,name,place):
#         self.name=name
#         self.place=place
#     def house_display(self):
#         print(self.name,self.place) 


# house_instance=house("rif","nand")
# house_instance.house_display()


