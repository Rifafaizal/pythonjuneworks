text="rif rhmth fizl faia mifr"
#print first recursive(repeat) character


#word_count
#stp1-split the string
words=text.split(" ")  #lst ayt therum
word_count={}
for w in words: #hello
    if w in word_count:
        word_count[w]+=1
    else:
        word_count[w]=1
print(word_count)

