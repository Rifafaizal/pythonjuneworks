start_limit=int(input("enter start limit"))
end_limit=int(input("enter end limit"))
for i in range(start_limit,end_limit):
    if(i%2!=0):
        print(i)
        i=i+1
        
