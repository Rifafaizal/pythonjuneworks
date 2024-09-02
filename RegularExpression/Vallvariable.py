#Q)first character must be an alphabe=>k to m
#secon letter must be a num that is \(divisible)3
#followed by  any number of alphabets and numbers @
from re import fullmatch


variable_name=input("enter a variable")


pattern="[k-m][369][a-zA-Z0-9]"

matcher=fullmatch(pattern,variable_name)

if matcher==None:

    print("invalid")

else:

    print("valid")


