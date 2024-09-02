text="ABCCDDBB"
word_count={}  #dict
for c in text:   #a-1,b-1,c-1
    if c in word_count:
        print(c,"first recursive character")  #key c variable l enthANO ATH SETT CHEYYUM
        break
    else:
        word_count[c]=1  #1 AYT SET CHEYYUM.key ayt c(charcter)ne set cheyyum
        