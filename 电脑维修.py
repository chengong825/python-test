n=10
m=10#电脑阵列4行7列

badcomputers=[[0, 0], [0, 9], [1, 7], [2, 3], [6, 4]]
x=len(badcomputers)
print(len(badcomputers))
badcomputers.sort()
count=0
while count<x and badcomputers[count][0]==badcomputers[0][0]:
    count+=1
minleft= 2 * badcomputers[count - 1][1]#第一个坏点的左边最小距离
minright=m-1#第一个坏点的右边最小距离
i=badcomputers[count - 1][0]
x1=count
print(minleft,minright)
while i<n:
    count=0
    while x1<x and i==badcomputers[x1][0]:
        x1+=1
        count+=1
    if count:
        minleft=min(minleft + 2 * badcomputers[x1 - 1][1], minright + m - 1)
        minright=min(minleft + m - 1, minright + 2 * (m - 1 - badcomputers[x1 - count][1]))
    print("第%d行左边距离最小值%d，右边距离最小值%d" % (i, minleft, minright))
    i+=1
print(min(minleft,minright)+n-1)
print(badcomputers)
