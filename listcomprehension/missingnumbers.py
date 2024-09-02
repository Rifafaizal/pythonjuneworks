#fnd missing positive numbers
arr=[0,1,3,4]
#prvs current   utility functions:input(),print(),sorted(),type(),len(),round(),max(),min(),sum()
# cr-pr==1 ahnonn check cheyyuka
#n(n+1)/2
# sum=4(4+1)/2=4*5/2=20/2=10
# total=8
# 10_8=2
# cur_sum=7
# 10-7=3
n=len(arr)

sum_of_n=n*(n+1)/2
current_sum=sum(arr)
missing_number=sum_of_n-current_sum


print(missing_number)
x=3.456
print(round(x))

#find previous and current missing numbers