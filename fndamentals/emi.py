# write a prgrm to find emi
# loan amount
# inerest
# loan tenure

# import math
# loan_amount=200000
# Interest=9
# tenure=36
# Interest_per_month=Interest/12/100

# Emi=loan_amount*Interest_per_month*(1+Interest_per_month)*tenure/(((1+Interest_per_month)*tenure)-1) 

#P x R x (1+R)^N / [(1+R)^N-1]
# P = Principal loan amount
# R = Rate of Interest per month ie percentage interest per anum/12/100
# N = Number of instalments every month

# Emi_round=round(Emi)
# Emi_a=math.ceil(Emi)
# Emi_b=math.floor(Emi)
# print(f"The emi for a loan amount of {loan_amount} for an Interest of {Interest}% for {tenure} month is {Emi}")
# print(f"Rounded Emi per month is {Emi_round} , {Emi_a} and {Emi_b}")

# print(f"The emi for a loan amount of {loan_amount} for an Interest of {Interest}% for {tenure} month is {round(Emi)}")


# #toal inerest payable
# total_payable_amount=Emi*n
# print(f"MONTHLY Emi={Emi}")
# print(f"total payable amount={total_payale_amount}")
# total_intrest_payable=total_payable_amount-loan_amount
# print(f"total interest payable amountt={total_interset_payable}")



#2ime:
# write a prgrm to find emi
#emi= [p x r x (1+r)**n] / [(1+r)**n - 1]
#p=> loan amount
#r=>interest
# t=>tenure(years)=>months

#set loan_amount
loan_amount=200000
#set interest_rate
interest_rate=9
#set tenure(period)
tenure=10

#convert yearly interest rate to monthly interest rate
r=interest_rate/100/12

#convert tenure in years to month
n=tenure*12  #monthly
one_plus_r=(1+r)**n
emi=(loan_amount*r*one_plus_r)/(one_plus_r-1)
total_payable_amount=emi*n
print(f"monthly emi={emi}")
print(f"total payable amount{total_payable_amount}")

temp_in_deg=35

#(0°C × 9/5) + 32 = 32°F
# temp_in_fh=(temp_in_deg*(9/5)) + 32
# print(f"{temp_in_deg}degree={temp_in_fh}fh")






