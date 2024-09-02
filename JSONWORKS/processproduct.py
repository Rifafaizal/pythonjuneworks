from json import load
f=open("C:\\Users\\ser\\Desktop\\PythonJuneWorks\\JSONWORKS\\product.json",encoding="UTF-8")  #8 means bit
items=load(f)
# print(items)
#items=[{},{},,,,,,,,{}]  #utf-char encoding prgrm
# arr=[10,20,30]
# print(len(items))

#-----------------------------------------------------------------
# for i in items:
    # print(i.get("title"))


#---------------------------------------------------------------

# items_title=[ i.get("title") for i in items]

# print(items_title)

#-----------------------------------------------------------------------------



jwelery_items=[ i.get("title") for i in items if i.get("category")=="jewelery"]
# print(jwelery_items)

#---------------------------------------------------------------------------

men_cloth=[i.get("title") for i in items if i.get("category")=="men's clothing"] 
# print(men_cloth)

#-----------------------------------------------------------------------------

item_price=[i.get("title") for i in items if i .get("price")>999]
# print(item_price)

#----------------------------------------------------------------------------


item_id=[i.get("description") for i in items if i.get("id")==15]
# print(item_id)

#---------------------------------------------------------------------------------


#prdct  in range of 100-150
item_price=[i.get("title") for i in items if i.get("price")>=100 and i.get("price")<=150]
# print(item_price)

#----------------------------------------------------------------------------------------------


item_price=[i.get("id") for i in items if i.get("price")>=100 and i.get("price")<=500]
# print(item_price)

#floating point numbers greaterthan that cvase l count akoola.range nte case l cpount aakum(range floting numbers consider cheyyoola,greater than thats pkke consuder cheyyum)

item_price=[i.get("id") for i in items if i.get("price") in range(100,500)]
# print(item_price)

#------------------------------------------------------------------------------------------------------



#item with most number of rating

def get_rating_count(dic) :
    return dic.get("rating").get("count")
top_most_rating_item=max(items,key=get_rating_count)
# print(top_most_rating_item)
# print(top_most_rating_item.get("title"),top_most_rating_item.get("rating").get(("count")))

#--------------------------------------------------------------------------------------------


#item with min num of rating
def get_rating_count(dic):
    return dic.get("rating").get("count")
min_rating_item=min(items,key=get_rating_count)  
print(min_rating_item.get("title"),min_rating_item.get("rating").get("count"))



#----------------------------------------------------------------------------------------------------

