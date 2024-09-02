from re import finditer
text="12ab45cd5rf@$35"
#c-h or t-z-[c-ht-z]
pattern="([a-z]{2}|[0-9]{2})"
#or([c-h]|[t-z]),numberkodkkanel ([c-h]{2}|[t-z]{3}) or ([c-h]{2})
matcher=finditer(pattern,text)
for m in matcher:
    print(m.start(),"   ",m.group())