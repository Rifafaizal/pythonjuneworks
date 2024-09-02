from json import load
f=open("C:\\Users\ser\\\Desktop\\PythonJuneWorks\\JSONWORKS\\films.json","r")
films=load(f)
# print(films)
for fl in films:
    print(fl.get("title"))