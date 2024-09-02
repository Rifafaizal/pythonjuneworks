text="ABABCDE"
#PRNT ALLL non recursive character
word_count={}
for ch in text:
    if ch in word_count:
        word_count[ch]+=1
    else:
        word_count[ch]=1
for k,v in word_count.items():   #a-2,b-2,c-1,d-1,e-1
    if v==1:
        print(k)

