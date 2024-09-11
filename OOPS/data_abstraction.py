from abc import ABC,abstractmethod
class car(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def accelerate(self):
        pass
    @abstractmethod
    def stop(self):
        pass
class innova(car):
    def start(Self):
        print("start method") 
    def accelerate(self):
        print("accelerate method")
    def stop(self):
        print("stop method") 
innova_instance=innova()
innova_instance.start()
innova_instance.accelerate()
innova_instance.stop() 

#editor prgrm

from abc import ABC,abstractmethod
class editor(ABC):
    @abstractmethod
    def execute(self):
       pass
    @abstractmethod
    def run(self):
       pass

class pycharm(editor):
    def execute(self):
        print("execute method")
    def run(self):
        print("run method")
pycharm_instance=pycharm()
pycharm_instance.execute()
pycharm_instance.run()






