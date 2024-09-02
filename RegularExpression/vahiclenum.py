#must ayt kodkkndiye sadanm paranthesis() vechittan kodkkndiye
from re import fullmatch

vehicle_num=input("enter vehicle")

pattern="(KL)(-)?[0-9]{2}(-)?[A-Z]{1}(-)?[0-9]{4}"   #?-ONE CHAR OPTIONAL

matcher=fullmatch(pattern,vehicle_num)

print("invalid" if matcher==None else "valid")


