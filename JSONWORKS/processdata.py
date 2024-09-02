from json import load
f=open("C:\\Users\\ser\\Desktop\\PythonJuneWorks\\JSONWORKS\\data.json","r")
prod=load(f)

# print(prdcts)
for p in prod:
    # print(p.get("title"))
product_data=[p for p in prod if p.get("title")=="s23"][0] 
print(prod_data)   

