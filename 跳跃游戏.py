def fun(arr):
    i=0
    max=arr[i]
    while i<=max and i<len(arr):
        if i+arr[i]>max:
            max=i+arr[i]
        i+=1
    if max>=len(arr)-1:
        return True
    else:
        return False
a=[3,2,1,1,4]
print(fun(a))