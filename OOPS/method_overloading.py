#*args kodthal overload cheyyandiye avshym illa.data tuple format l edtholm

# class operations:
#     def perform_add(self,*args):
#         return sum(args)
#     def perform_max(self,*args):
#         return max(args)
#     def perform_min(self,*args):
#         return min(args)    
# instance_math=operations()
# print(instance_math.perform_add(10,30,20))
# print(instance_math.perform_add(10,30,20,50))
# print(instance_math.perform_max(10,60)) 
# print(instance_math.perform_min(10,60)) 






# isinstance-pass cheyyne value check cheyyan
# class operations:
#     def perform_add(self,*args):
#         total=sum([arg for arg in args if isinstance(arg,(int,float))])
#         return total
       
#     def perform_max(self,*args):
#         total=max([arg for arg in args if isinstance(arg,(int,float))])
#         return total 
# instance_math=operations()
# print(instance_math.perform_add(10,30,30.5,40.5))  
# print(instance_math.perform_max(10,30,30.5,40.5)) 



# **kwargs-two ** kodthal athine dictionary format l display cheyyum(keyword arguments)

# class operations:
#     def get_person(**kwargs):

#         print(kwargs.get("name"))
#         print(kwargs.get("place"))
#     get_person(name="rifa",place="nandi",country="india") 
       
        



#flat list prgrm

# def flat_list(*args):
#     flat=[]
#     for arg in args:
#         if isinstance(arg,list):
#             flat.extend(flat_list(*arg))
#         else:
#             flat.append(arg)
#     return flat



    
# print(flat_list(1,2,[2,3],[10,[11,12]]))


print(isinstance(10,int))

