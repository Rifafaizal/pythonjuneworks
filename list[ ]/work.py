#1)wap to find the sum of odd numbers in the list
#2)wap to find the count of even and odd numbers in the list


#1)
num=[1,7,8,2]
odd_total=0
for i in range(0,len(num)):
    if num[i]%2!=0:
        odd_total=odd_total+num[i]
print(odd_total)


