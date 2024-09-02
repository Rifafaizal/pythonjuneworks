#create a dictnry mobile with keys nam,e,brand,price,is_available
mobile={"name":"iphone","brand":"moto","price":7700,"is_available":True,"offer":1000}



#prnt mobile name
#cls dict:get(key)=>return value
# print(mobile.get("name"))
# print(mobile.get("brand"))
# print("task1")

#keys()=>return all keys
# all_keys=mobile.keys()
# print(all_keys)


#values
# all_values=mobile.values()
# print(all_values)

#item
# for k,v in mobile.items():
#     print(k,v)

#pop(key)
# popp_elememt=mobile.pop("name")
# print(popp_elememt)
# print(mobile)

# or
# mobile.pop("name")
# print(mobile)



#discount:100
# mobile["discount"]=100
# print(mobile)

# mobile["price"]=100
# print(mobile)  #value change aakum

#sellng price
if "offer" in mobile:
    selling_price=mobile.get("price")-mobile.get("offer")
    print(selling_price)
else:
    selling_price=mobile.get("price")
    print(selling_price)
        







#key exist or not
# print("name" in mobile)  #true  or false    OR
# if "sell" in mobile:
#     print("valid")
# else:
#     print("invalid")

    










