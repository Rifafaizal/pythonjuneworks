#prgrm to cjeck numbr is palindrome or not
#121 is palimdrome number
#123 is not palindrome


num=int(input("enter a number"))
result=0
org=num
while(num!=0):
    digit=num%10
    result=result*10+digit
    num=num//10
print(f"palindrome" if result==org else "not palindrome")
