#read a year from  user and 
# print century year if year ends with zero
#else orint non century year


year=int(input("enter year"))
if year%100==0:
    print("century year")
else:
        print("non century year")

