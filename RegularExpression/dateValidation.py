from re import fullmatch


date_var=input("enter a date")


pattern="(0[1-9]|1[0-9]|2[0-9]|3[0-1])"


matcher=fullmatch(pattern,date_var)

print("invalid" if matcher==None else "valid")

