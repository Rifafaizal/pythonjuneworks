weight_in_kg=(int(input("enter weight")))
height_in_cm=(int(input("enter height")))
height_in_meter=height_in_cm/100
bmi=(weight_in_kg/height_in_meter**2)
print(f"weight {weight_in_kg} height {height_in_meter} bmi {bmi}")