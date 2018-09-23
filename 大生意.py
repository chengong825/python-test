a=[3,1,5]
b=[4,3,100]
arr=[(a[i],b[i]) for i in range(0,len(a))]
arr.sort()
print(arr)
k=10
for x in range(0,len(a)):
    if k>=arr[x][0] and arr[x][1]>arr[x][0]:
        k+=arr[x][1]-arr[x][0]
print(k)


