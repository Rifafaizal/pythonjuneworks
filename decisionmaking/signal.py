#read a signal
# print stop if color is red
# print go if color is green
# print wait if color is orange
#else print invalid


signal=input("enter signal")
if signal=="red":
    print("stop")
elif signal=="green":
    print("go")
elif signal=="orange":
    print("wait")
else:
    print("invalid")

