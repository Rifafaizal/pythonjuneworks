def is_disarium(num):
    
    exp = len(str(num))
    val = num
    res = 0
    
    while num != 0:
        
        digit = num%10
        res += digit ** exp
        num = num//10
        exp -= 1
        
    return res == val


num = int(input("Enter a number: "))
print(is_disarium(num))