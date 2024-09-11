class person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def display(self):
        print(self.name,self.age,self.gender) 
class employee(person):
    def __init__(self,name,age,gender,eid,department,salary):
        super().__init__(name,age,gender)
        self.eid=eid
        self.department=department
        self.salary=salary
    def dispaly(self):
        super().display()
        print(self.eid,self.department,self.salary)
employee_instance=employee("hheri",34,"male",133,"bba",1200)
employee_instance.display()



