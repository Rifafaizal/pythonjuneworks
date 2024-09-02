
num1=(int(input("enter the first number")))    
num2=(int(input("enter the second number")))
num3=(int(input("enter the third number")))
if num1>num2>num3 or num3>num2>num1:           
    print(f"num2 {num2}is the second largest")   


elif num1>num3>num2 or num2>num3>num1:          
    print(f"num3 {num3}is the second largest")   


elif num3>num1>num2 or num2>num1>num3:          
    print(f"num1 {num1}is the second largest") 