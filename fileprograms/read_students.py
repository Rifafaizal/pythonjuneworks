f=open("C:\\Users\\ser\\Desktop\\PythonJuneWorks\\fileprograms\\students.txt","r")
students=[]
for std in f:
    students.append(std.rstrip+("\n"))

print(students)