class grandparent:
    def m1(self):
        print("grandparent method")
class parent:
    def m2(self):
        print("parent method") 
class child(grandparent,parent):
    def m4(self):
        print("childclass method")  
child_instance=child()  
child_instance.m1()
child_instance.m2()
child_instance.m4()               