# 1st character upper case alphabet
# next characyer digit from 1-9
# next digit 0-9
# 4th place 0 or 1 space
# next 4 character any number from 0-9 
# last character 1-9

#S71 19937
from re import fullmatch


passport_num=input("enter num") 


pattern="[A-Z][1-9][0-9][0\s][0-9]{4}[1-9]"


matcher=fullmatch(pattern,passport_num)


print("invalid" if matcher==None else "valid")
