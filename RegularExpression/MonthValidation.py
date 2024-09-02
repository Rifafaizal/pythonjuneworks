#validate_month
from re import fullmatch


month_val=input("enter month")

pattern="(0[1-9]|1[0-2])"

matcher=fullmatch(pattern,month_val)

print("invalid" if matcher==None else "valid")