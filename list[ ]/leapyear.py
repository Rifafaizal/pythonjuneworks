year=[1000,2000,3000,4000,4500,5000]
#print leap years from years list
for i in range(0,len(year)):
    if year[i]%100==0 and year[i]%400==0 or year[i]%100!=0 and year[i]%4==0:
        print (year[i])
