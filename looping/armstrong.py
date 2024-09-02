num=int(input("enter a number"))
original=num
total=0
digit_count=len(str(num))
while(num!=0):
    digit=num%10
    exponent=digit**digit_count
    total=total+exponent
    num=num//10 
print(total)
print("armstrong number" if original==total else "not armstrong")


#or
#if(org==0)
# print("armstrong number")
# else:
#     print("not armstrong")

 



