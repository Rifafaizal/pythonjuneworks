class grandparent:
   def m1(self):
    print("grandparent m1")
class parent(grandparent):    
   def m2(self):
    print("parent m2")
class child(parent):
    def m3(self):
     print("child m3")
child_instance=child()
child_instance.m2() 
child_instance.m3()
child_instance.m1()    
