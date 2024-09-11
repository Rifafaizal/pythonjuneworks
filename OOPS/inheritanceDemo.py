#parent class childlek inherit cheyya

class vehicle:
    def start(self):
        print("start method")
    def accelerate(self):
        print("accelerate method")

class innova(vehicle):
    pass

innova_instance=innova() 
innova_instance.accelerate()
innova_instance.start()




#super instance-parent nte constructor call cheyyn