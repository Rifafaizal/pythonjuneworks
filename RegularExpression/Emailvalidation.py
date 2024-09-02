# +(match one OR MORE )
# ?(optional)
# *(zero or more)

from re import fullmatch



email_id=input("ente email")



pattern="\w[\w\.&]*@gmail.com"



matcher=fullmatch(pattern,email_id)



print("invalid" if matcher==None else "valid")
