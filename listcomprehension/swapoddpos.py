arr=[2,3,4,5,6,7,8,9]
#odd_pos_num=[3,5,7,9]
# reverse_odd_pos_num==[9,7,5,3]
#[14,13,11,7,5,3]   even position l llathin no changwe
left=1
length=len(arr)-1 #8-1=7
if length%2!=0:
    right=length
else:
    right=length-1
    while(left<right):
        (arr[right],arr[left])=(arr[left],arr[right])
        left=left+2
        right=right-2
print(arr)

# missing pos integer
#nesed collection





