words=["hello","hai","hello","hai","hai"]



#prnt word count
# word_set=set(words)   #hello,hai
# for w in word_set:
#     print(w,words.count(w))


#another method for find countt
word_count={}
for w in words:     #w=helo
    if w in word_count:
        word_count[w]+=1
    else:
        word_count[w]=1
print(word_count)

    