# text="setiplngdfhjueiogfgsoithkk"
# vowels="aeiou"
# v_count=0
# for ch in text:   
#     if vowels.count(ch)!=0:
#         v_count+=1
# print(v_count)    



#another method

# text="setiplngdfhjueiogfgsoithkk"
# vowels="aeiou"
# v_count=0
# for ch in vowels:   #ch=a
#     v_count+=text.count(ch)
# print(v_count)


#print vowels and comsonants
text="haimrning"
vowels="aeiou"
v_count=0
c_count=0
for ch in text:
    if vowels.count(ch)!=0:
        v_count+=1
    else:
        c_count+=1
print(f"vowels={v_count}") 
print(f"consonants={c_count}")       
