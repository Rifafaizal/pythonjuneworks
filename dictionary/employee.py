employee={"name":"hari","dept":"red","salary":9000,"combo_offer":1000,"extra_working_days":5}



#prnt all key values
for k,v in employee.items():
    print(k,v)


#extra_working   days present
# if("extra_working_days" in employee ):
#     print("present")
# else:
#         print("not present")





#prnt employees netpay
if ("extra_working_days" in employee):
    net_pay=employee.get("salary")+employee.get("combo_offer")*employee.get("extra_working_days")
    print(net_pay)
else:
        net_pay=employee.get("price")
        print(net_pay)



# fetching value from  dictnry using key >= dict.get(key)
# adding new key value pair>=dict[key]=value       


    