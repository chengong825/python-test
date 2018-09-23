a=[1,2,3,-5,-6]
a.sort()
print(a)
max1=a[len(a)-1]
max2=a[len(a)-2]
max3=a[len(a)-3]
min1=a[0]
min2=a[1]
min3=a[2]
max=max1*max2*max3
if max<min1*min2*max1:
    max=min1*min2*max1

print(max)