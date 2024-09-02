#wapt to find secondlargest with method
# num=[1,2,4,6,9,10,12]
# largest_num=0
# second_largest_num=0
# for i in num:
#     if i>second_largest_num and i>largest_num:
#         second_largest_num=largest_num
#         largest_num=i
# print(second_largest_num)


      #OR

num=[15,2,4,6,9,10,12]
largest_num=0
second_largest_num=0
for i in num:
    if i>second_largest_num and i>largest_num:
        second_largest_num=largest_num
        largest_num=i
    elif i>second_largest_num and i<largest_num:
        second_largest_num=i

print(second_largest_num)








#wap to  find secondlargest for using methods
# num=[15,2,4,6,9,10,12]
# num.sort()
# print(num[-2])






