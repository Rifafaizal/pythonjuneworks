arr=[
    [10,19],
    [21,30],
    [40,50]
]
# numbers=[num for lst in arr for num in lst]
# print(sum(numbers))
# evens=[num for lst in arr for num in lst if num%2==0]
# print(evens)
# odd=[num for lst in arr for num in lst if num%2!=0]
# print(odd)
# num_gt_40=[num for lst in arr for num in lst if num>40]
# print(num_gt_4)






mobiles=[

    {"id":100,"title":"s23 ultra","brand":"samsung","price":12500,"network":"5g"},
    {"id":101,"title":"s23","brand":"samsung","price":54000,"network":"4g"},
    {"id":102,"title":"edge14pro","brand":"moto","price":25000,"network":"5g"},
    {"id":103,"title":"edgeneo","brand":"moto","price":22000,"network":"4g"},
    {"id":104,"title":"redminote13pro","brand":"mi","price":25000,"network":"5g"},
    {"id":105,"title":"redmi13","brand":"mi","price":12000,"network":"4g"},
]


#print all mobile names
# all_mobile_names=[mb.get("title")for mb in mobiles]
# print(set(all_mobile_names))





#print all brands
# all_brand_names=[mb.get("brand")for mb in mobiles]
# print(set(all_brand_names))





#print samsung mobile names
# samsung_mobile_names=[mb.get("title")for mb in mobiles if mb.get("brand")=="samsung"]
# print(set(samsung_mobile_names))







#print all  mobiles price range is 23000-40000
# price_range=[mb.get("title")for mb in mobiles if mb.get("price")in range(23000,40000)]
# print(price_range)






#find max  price

def get_price(mob):
    return mob.get("price")
# costly_prce=max(mobiles,key=get_price)
# print(costly_prce)

#min function
# cheap_prce=min(mobiles,key=get_price)
# print(cheap_prce)


#sorted
# sorted_mobl=sorted(mobiles,key=get_price,reverse=True)
# print(sorted_mobl)


#sum
total_cost=sum([mob.get("price")for mob in mobiles])
print(total_cost)













