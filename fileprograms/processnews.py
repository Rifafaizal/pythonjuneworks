f=open("C:\\Users\ser\\\Desktop\\PythonJuneWorks\\fileprograms\\news.txt","r")
# wordlst=[]
# for line in f:
#     words=line.rstrip("\n").split(" ")
#     for w in words:
#         wordlst.append(w)
# print(wordlst)
# word_count={w:wordlst.count(w) for w in wordlst}
# print(word_count)
# def val(key):
#     return word_count.get(key)
# sort=sorted(word_count,key=val,reverse=True)
# print(sort)






wrdlst=[]
for line in f:
    words=line.rstrip("\n").split(" ")   #split
    for w in words:
        wrdlst.append(w)
print(wrdlst)       
wordcount={w:wrdlst.count(w) for w in wrdlst}
print(wordcount)
def rifa(key):    #rifa-key nte name
    return wordcount.get(key)
srt=sorted(wordcount,key=rifa,reverse=True)
print(srt)
# print(srt[0])

