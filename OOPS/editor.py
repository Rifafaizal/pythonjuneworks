class editor:
    def __init__(self,name,logo):
        self.name=name
        self.logo=logo
    def open(self):
        print(f"{self.name} open")  
    def execute(self):
        print(f"{self.name} execute") 
class vscode(editor):
    def __init__(self,name,logo):
        super(). __init__(name,logo)
vscode_instance=vscode("vscodeedit","hihi") 
vscode_instance.open()    

