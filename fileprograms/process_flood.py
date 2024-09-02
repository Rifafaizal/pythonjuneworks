f=open("C:\\Users\\ser\\Desktop\\PythonJuneWorks\\fileprograms\\flood.txt","r")
dta=[]
for line in f:
    list=line.rstrip("\n").split(" ")
    dict={"state":list[0],"year":list[1],"death_count":int(list[2])}
    dta.append(dict)
    # print(dta)



#ellam dictionarylekk matti.list of dictionary 




#-------------------------------------------------------------------------------------------
#  1)death per state

death_per_state={}
for dict in dta:
    state=dict.get("state")
    death_count=dict.get("death_count")
    if state in death_per_state:
        death_per_state[state]+=death_count
    else:
        death_per_state[state]=death_count
# print(death_per_state)


#------------------------------------------------------------------------------------------------
# 2)death_per_year
death_per_year={}
for  dict in dta:
    year=dict.get("year")
    death_count=dict.get("death_count")
    if year in death_per_year:
        death_per_year[year]+=death_count
    else:
        death_per_year[year]=death_count
print(death_per_year)




