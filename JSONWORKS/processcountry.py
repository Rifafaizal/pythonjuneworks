from json import load
f=open("C:\\Users\\ser\\Desktop\\PythonJuneWorks\\JSONWORKS\\country.json",encoding="UTF-8")
country=load(f)
# print(country)
# print(len(country))
#------------------------------------------------------------


#1)country names print cheyya
# country_names=[ c.get("name")for c in country]
# print(country_names)


#----------------------------------------------------------------------
#2)find the details of country india
def fetch_by_data(name):
    return[ c for c in country if c.get("name")==name][0]
country_data=fetch_by_data("India") 
# print(country_data)

#---------------------------------------------------------------------------

#eg
country_capitals=[
        {"name":"india","capital":"delhi"},
        {"name":"englnd","capital":"kabul"},
        {"name":"srilnka","capital":"colombo"},
        {"name":"china","capital":"bijing"}
]

# c_data=[ c for c in country_capitals if c.get("name")=="india"][0]
#list ne oyivakkan-[0]
# print(c_data)

#-------------------------------------------------------------------------------------------










#---------------------------------------------------
#3)highest area
# def get_area(dic):
#     if "area" in dic:
#         return dic.get("area")









#4)english lang ayt varnne country names
# for c in country:







#---------------------------------------------------------------------------------------------------------
#5)largest region by area

# all_region={c.get("region") for c in country }
# print(all_region)
# region_sumary={}
# for c in country:
#     region_name=c.get("region")
#     if region_name in region_sumary:
#         region_sumary[region_name]+=c.get("area",0)
#     else:
#         region_sumary[region_name]=c.get("area",0)
# # print(region_sumary)
# value_key=[(v,k)for k,v in region_sumary.items()] 
# print(max(value_key))


#-----------------------------------------------------------------------------------------------------------
#6)highest population varunna countries
# def highest_population(key):
#     return key.get("highest_population")
# highest_population_countries=max(country,key="highest_population") 
# print(highest_population_countries)


#--------------------------------------------------------------------------------------




#7)population 20000 n above lla names print cheyya
# for c in country:
#     country_population=[ c.get("name")for c in country if c.get("population")>20000]
# print(country_population)



#--------------------------------------------------------------------------------------------
#8)

# for c in country:
#     country_area=[c.get("name") for c in country if c.get("area") in range(100,550)]
# print(country_area)


#-------------------------------------------------------------------------------------------
#9) other names
def fetch_by_data(name):
    return[ c for c in country if c.get("name")==name][0]
country_data=fetch_by_data("Barbados") 
# print(country_data)
if "regionalBlocs" in country_data:
    blck_data=country_data.get("regionalBlocs")[0]

# print(blck_data)
    if "otherNames" in blck_data:
        print(blck_data.get("otherNames"))
    else:
        print(blck_data.get("otherNames"))
        









 





