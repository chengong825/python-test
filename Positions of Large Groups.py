S="aaabbbaxcascccc"
a = []
j = 0
while j < len(S):
    i = j + 1
    count = 1
    while i < len(S):
        if S[i] == S[j]:
            count += 1
            i += 1
        else:
            break
    if count >= 3:
        a.append([j, i - 1])
    j = i
print(a)