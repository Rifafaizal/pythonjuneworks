# create a fumction nth_digit_max with two parameter num1,num2
# nth_digit_max(123,480)=>123
# nth_digit_max(546,127)=>127      last digit l valth

def nth_digit_max(num1,num2):
    return num1 if num1%10 > num2%10 else num2
print(nth_digit_max(123,480))


or

