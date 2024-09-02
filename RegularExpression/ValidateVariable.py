#eg:[a-z]*-(* kodthal optional aayirikkm)
#{}-count
#()-const aytlle,must
from re import fullmatch

validate_var=input("enter a var")

pattern="[a-zA-Z][a-zA-Z0-9]"


matcher=fullmatch(pattern,validate_var)


if matcher==None:


    print("invalid")


else:


    print("valid")

