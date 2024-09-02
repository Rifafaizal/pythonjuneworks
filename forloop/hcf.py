#hcf of (12,24) #1,2,3,4,6,123,(12)
##1,,,,,12
#alt shift down

num1=int(input("enter a number"))
num2=int(input("enter a number"))
gcd=11
for i in range(1,num1+1):
 if(num1%i==0) and num2%i==0:
    gcd=i
    print(gcd)