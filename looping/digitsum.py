#read a number print sum of digit
#input=543
#output
num=int(input("enter num"))
total=0   
while(num!=0):
    digit=num%10
    total=total+digit
    num=num//10
print(total)

