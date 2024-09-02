#write a prgrm to convert temp in celcius to temp in fh
#read temp in celsius from the user

temp_in_deg=(int(input("enter temperature in degree")))

#(0°C × 9/5) + 32 = 32°F
temp_in_fh=(temp_in_deg*(9/5)) + 32
print(f"temperature in fh{temp_in_fh}") 