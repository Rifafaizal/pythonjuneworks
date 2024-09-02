numbers=(1,2,3,4)        #representing method.tuple.defined by(),
print(numbers[3])     #index psitioning,duplicates allowed,immutable,index(),count()



numbers=[1,2,[3,(100,200,300),4],5,6]
num=numbers[2][1]   #(100,200,300)
new_num=list(num)  # [100,200,300]
new_num.append(500) #[100,200,300,500]
numbers[2][1]=tuple(new_num)   #[1,2,[3,(100,200,300,500),4],5,6]
print(numbers) 

