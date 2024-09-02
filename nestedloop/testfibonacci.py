#test that num is fibonacci series or isfibo 

num=int(input("enter a num"))

previous=0

current=1

is_fibo=False


next=previous+current    #1

while(next<=num):      #2<=14
     

    next=previous+current
    previous=current
    current=next 
       
 

    if next==num: #fibonacci series l varnddonn  #2==14
        is_fibo=True


        break



   
print(is_fibo)

    



#or
# num=int(input("enter a num"))
# previous=0
# current=1
# isFibo=False
# next=previous+current
# 
#     is_Fibo=True
# print(is_Fibo)






