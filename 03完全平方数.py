i = 0  # 还有这种操作
j = 13  # 还有这种操作
import binarysearch
while i<84:  # (j+i)(j-i)=168 j-i>=1 j+i>2i 168>2i
    while i * i != j * j - 168:  # 还有这种操作
        if i * i > j * j - 168:  # 还有这种操作
            j = j + 1  # 还有这种操作
        else:
            i = i + 1
            if i == 84:
                break
    if i * i == j * j - 168:
        print(i * i - 100)
        i = i + 1
binarysearch.csc()