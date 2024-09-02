#{start}{group}
from re import finditer
text="faizghfhgjkmfaizhgjkmnfaizjhfaiz"
match_faiz=finditer("faiz",text)
for m in match_faiz:
    print(m.start(),"@@",m.group())
#finditer-ethokke place l match nd nn    