#same function or method name and different parametes or arguments

# def add_numbers(n1,n2):
#     return n1+n2
# print(add_numbers(200,300))

# def add_numbers(n1,n2,n3,n4):
#     return n1+n2+n3+n4
# print(add_numbers(12,34,45,77))  
#args=>tuple


#tuple -in tuple case oru number kodkkmbol eg(10)kodkkanel print cheyyumbo (10,) varm. bracketl *args kodkkmbol ath tuple aytan consider cheyyuka
def add_prgrm(*args):
    print(min(args))
add_prgrm(10,20)


def adds_person(*args):
    print(sum(args))
adds_person(10,30,2,38)    

