# numbers=[1,2,[3,[100,200,300],4],5,6]
# print(numbers[2])   #[3,[100,200,300]4]
# print(numbers[2][1])   #[100,200,300]
# numbers[2][1].append(800)   #[100,200,300,800]
# print(numbers)




#write a prgrm to swap first and last element in a list
# num=[1,4,5,7]
# num[0],num[3]=num[3],num[0]
# print(num)

num=[1,4,5,7]
num.pop(-1)
num.pop(0)
num.append(1)
num.insert(0,7)
print(num)








#return the odd numbers in the another list
# num=[1,7,9,5,8,9]
# odd_num=[]
# for i in num:
#     if i%2!=0:
#         odd_num.append(i)
# print(odd_num)


#wap tp remove the even number
# num=[1,2,3,4,5,6,7,8]
# for i in num:
#     if i%2==0:
#         num.remove(i)
# print(num)



#wap to print unique numbers
# num=[1,2,2,4,5,4,7,6,6]
# for i in num:
#     if num.count(i)==1:
#         print(i)

        



