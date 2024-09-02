#write a prgrm to calculate
  #monthly emi
  #total payment
   #total interest payable
   #read loan amnt,tenure,intrst rate from the user
loan_amount=(int(input("enter  loan amount")))
interest_rate=(int(input("enter interest rate")))
tenure=(int(input("enter tenure")))

r=interest_rate/100/12
n=tenure*12

one_plus_r=(1+r)**n


emi=loan_amount*r*one_plus_r/one_plus_r-1

print(f"emi{emi}")

