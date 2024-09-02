loan_amount=(int(input("enter loan amount")))
tenure=(int(input("enter tenure")))
interest_rate=(int(input("enter interest rate")))

r=interest_rate/100/12
n=tenure*12

one_plus_r=(1+r)**n
emi=loan_amount*r*one_plus_r/one_plus_r-1
print(f"emi {emi}")