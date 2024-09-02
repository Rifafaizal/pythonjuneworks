#wrte prgrm to print bmi
#read height and weight from the user
#bmi=(weight_in_kg/height_in_meter square)
weight_in_kg=int(input("enter weight"))
height_in_cm=(int(input("enter height")))
height_in_meter=height_in_cm/100
bmi=(weight_in_kg/height_in_meter**2)
print(f"weight{weight_in_kg} height{height_in_meter**2}  bmi{bmi}")