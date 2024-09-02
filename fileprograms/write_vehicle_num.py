vehicle_numbers=["kl7898","kl754","kl9324"]
f=open("C:\\Users\\ser\\Desktop\\PythonJuneWorks\\fileprograms\\write_vehicle.txt","w")
for num in vehicle_numbers:
    f.write(str(num)+"\n")