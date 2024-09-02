#read a number and extract digits from number
#sample input1 num=123


num=int(input("enter a number"))   #483
while(num!=0):
    digit=num%10   #483%10
    print(digit)   #prnt
    num=num//10    #483//10