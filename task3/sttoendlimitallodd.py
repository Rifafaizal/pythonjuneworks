# read start limit and end limit from the user and print all the odd numbers from the start limit and end limit

start_limit=int(input("enter start limit"))
end_limit=int(input("enter end limit"))
i=start_limit
while(i<=end_limit):
    if(i%2!=0):
        print(i)
    i=i+1
