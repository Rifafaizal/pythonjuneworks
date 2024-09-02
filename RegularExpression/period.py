#findall-The .findall() method iterates over a string to find a subset of characters that match a specified pattern. It will return a list of every pattern match that occurs in a given string.
#.at - .at kodthal at  nte munnil alphabets varnne print aakum(period- .)
from re import findall
text="irif and hirif are girif those lirif"
pattern=".irif"
matcher=findall(pattern,text)
print(matcher)