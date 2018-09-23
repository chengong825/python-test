def canConstruct(ransomNote,magzine):
    r=len(ransomNote)
    m=len(magzine)
    ls=[]
    for i in range(r):
        for j in range(m):
            if j not in ls:
                if ransomNote[i]==magzine[j]:
                    ls.append(j)
                    break
        else:
            return False
    return True
a='a'
b='ba'
print(canConstruct(a,b))