number=[1,2,[3,(100,200,300),4],5,6] 
num=number[2][1]
lst_num=list(num)
lst_num.remove(300)
number[2][1]=tuple(lst_num)

print(number)


