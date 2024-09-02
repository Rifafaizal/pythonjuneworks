weight_in_kg=(int(input("enter the weight in kg")))
height_in_cm=(int(input("enter the height in cm")))
height_in_meter=(height_in_cm)/100
bmi= (weight_in_kg) / height_in_meter**2
if bmi<19:
    print(f"{bmi}  under weight")
elif bmi>19 and bmi<25: 
    print(f"{bmi}  normal weight")
elif bmi>25 and bmi<30:
    print(f"{bmi}  over weight")  
else:
    print(f"{bmi}obesity")