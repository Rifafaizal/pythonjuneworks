arr=[5,7,8,9,6,3,4]
#[return iteration cndition]
#map if num > 5 => num+1 if num<5 => num-1
#[4,8,9,10,7,2,3]
mapped_list=[num+1 if num>5 else num-1 for num in arr]
print(mapped_list)