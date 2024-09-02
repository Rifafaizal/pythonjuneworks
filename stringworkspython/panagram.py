#all alphabets ndo nn check cheyyan
text="the quick brown fox jumps over a lazy dog"
alphabets="abcdefghijklmnopqrstuvwxyz"
#text lowerlekk matam
text=text.casefold()
is_Panagram=True
for ch in alphabets:
    if text.count(ch)==0:
        is_Panagram=False
        break
print(is_Panagram)
