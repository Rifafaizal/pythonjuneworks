#numbers=[1,2,[3,(100,200,300),4],5,6]>>>[1,2,[3,4],5,6]
# numbers=[1,2,[3,(100,200,300),4],5,6]
# nm=numbers[2]  #[3,(100,200,300),4]

# new=nm.pop()
# nm.insert(1,new)
# print(nm)
# numbers[2]=nm
# print(numbers)

# new_l=numbers[2][2]
# print(new_l)  #(100,200,300)
# n=list(new_l)
# n.insert(1,150)
# n1=tuple(n)
# numbers[2][2]=n1
# print(numbers)




#wap  to find second_smallest number without using methods
# numbers=[2,4,6,5,8,9,10]
# smallest_num=numbers[0]
# second_smallest=numbers[-1]
# for i in numbers:
#     if i < second_smallest and i < smallest_num:
#         second_smallest=smallest_num
#         smallest_num=i
#     elif i < second_smallest and i > smallest_num:
#         second_smallest=i
# print(second_smallest)



#wap to find second smallest with using method
numbers=[1,3,5,6,9,8]
numbers.sort()
print(numbers[1])






