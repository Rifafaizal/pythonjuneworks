#read a num from user
#print fizz if num is /by 3
#print buzz if num is /by 5
#print fizzbuzz if num is /by 15


num=(int(input("enter num"))) #15
if num%15==0:  #15%3==0  
    print("fizz")
elif num%5==0:
    print("buzz")
elif(num%3==0):
    print("fizzbuzz")


