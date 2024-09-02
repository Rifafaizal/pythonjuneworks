stud={"rifa":5,"thanzy":8,"mif":1}


def vlurr(key):
    return stud.get(key)



sort=sorted(stud,key=vlurr,reverse=True) 
print(sort)   