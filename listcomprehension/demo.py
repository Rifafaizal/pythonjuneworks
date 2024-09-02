# lst=[10,7,6,8,4]
# squares=[ lt**2 for lt in lst ]   #[return iteration condition]   10**2=100 7**2=49
# print(squares)

# cube=[ lt**3 for lt in lst ]   #[return iteration condition]   10**2=100 7**2=49
# print(cube)


#prnt even number frm list
# even_numbers=[ lt for lt in lst if lt%2==0 ]
# print(even_numbers)

#prnt odd numbers
# odd_numbers=[ lt for lt in lst if lt%2!=0 ]
# print(odd_numbers)



words=["fly","flyoff","flyin","flyout","out","in"]
# print list of words starting with fly
fly_words=[ w for w in words if w.startswith("fly") ]
print(fly_words)