def jug(n):
    m=n
    while m!=1:
        s=0
        while m:
            i = m % 10
            s = s + i * i
            m = m // 10
        m = s
        if m==4:
            break

    if m==1:
        return True
    else:
        return False
print(jug(555))