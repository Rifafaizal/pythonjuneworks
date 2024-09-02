#if condition:
      #stmt1
      #stmnt2
#else:
     #stmnt3
     #stmnt4
     
#read a signal from user[red,green,orange]
#red=>print stop
# green>=go
# orange>=wait

#read a number from user print odd if number is odd else print even
#set number
#condition number is even or odd

num=int(input("enter a number"))
if (num%2==0):
    print(f"{num} number is even")
else:
    print(f"{num} number is odd")
