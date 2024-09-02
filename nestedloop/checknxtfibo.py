#next fibonacci number
#num=14
# 10 prime numbers

num=int(input("enter a num"))

previous=0


current=1

next=previous+current

is_fibo=False

while(14<next):

    next=previous+current

    previous=current

    current=next

    if(next==num):

        is_fibo=True

        break

print(is_fibo)
