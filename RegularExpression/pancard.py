#validate pancard num
#first 3 character are alphabets
# 4 th place PCAFHT
# 5 th place alphabet
# 4 digit
# 1 alphabet


from re import fullmatch



pan_card=input("enter a number")


pattern="[A-Z]{3}[PCAFHT]{1}[A-Z]{1}[0-9]{4}[A-Z]{1}"


matcher=fullmatch(pattern,pan_card)


print("invalid" if matcher==None else "valid")