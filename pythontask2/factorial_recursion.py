# num=(int(input("enter a number  to find its factorial-")))
# if num<0:
#     print("factorial is not defines in negative numbers")
#     # factoprial-product all postve integers
# else:
#     print(f"factorial of {num} is {factorial(num)}")


def factorial(n):
    
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
    
num = int(input("Enter number: "))
print(factorial(num))