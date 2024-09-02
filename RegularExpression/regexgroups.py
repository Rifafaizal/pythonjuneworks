from re import finditer
text="abc456 @k#LMdehif"
# pattern="[^a-zA-Z0-9\s]"  #^-ithin shesham vere nthem kodthal ath display cheyyand opposite llath kanikkm aa data l lle
# pattern="[abf]"-check for either a b or f
# pattern="[a-k]"-check for albhabetss from a to k
# pattern="[A-Z]"-check all uppercase letters
# pattern="[0-9]"-check digits  for 0-9
#"\s"-space edkkan,"\S"-space exclude,\d"-digits edkkan,"\D"-digit exclude cheyyan(or [^0-9]),"\w"-[a-zA-Z0-9],"\W"-[^a-zA-Z0-9]
#\\d kodthalum work aavum
# matcher=finditer(pattern,text)
# for m in matcher:
#     print(m.start(),"===",m.group())
pattern="[\W]"
matcher=finditer(pattern,text)
for m in matcher:
    print(m.start(),"#",m.group())