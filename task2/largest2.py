#read three number from the user num1 num2 num3
#print largest
num1=(int(input("enter fist  number")))
num2=(int(input("enter second number")))
num3=(int(input("enter third number")))
if num1>num2 and num1>num3:
    print(f"{num1}is the largest number")
elif num2>num1 and num2>num3:
    print(f"{num2} is the largest")    
elif num3>num1 and num3>num2:
    print(f"{num3} is the largest") 
elif(num1==num2==num3):
      print(f"three numbers are equal")  
