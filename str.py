a='f155555'
c='1'

def fun(s,c):
    num = []
    i=0
    length=len(s)

    while i<length:
        j=0
        while i+j<length:
            if s[i+j]==c:
                min1=j
                break
            j+=1
        k=0
        while i-k>=0:
            if s[i-k]==c:
                min2=k
                break
            k+=1
        if i+j<length and i-k>=0:
            num.append(min(min1,min2))

        elif i+j>=length:
            num.append(min2)
        elif i-k<0:
            num.append(min1)
        i+=1
    return num
fun(a,c)
print(fun(a,c))
