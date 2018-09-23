# 括号的分数
# 给定一个平衡括号字符串 S，按下述规则计算该字符串的分数：
# () 得 1 分。
# AB 得 A + B 分，其中 A 和 B 是平衡括号字符串。
# (A) 得 2 * A 分，其中 A 是平衡括号字符串。
s='(())()'
# def score(s):
#     val=0
#     n=len(s)
#     for i in range(1,n):
#         pass
#     return val
def score(s):
    s_start = 0
    n = len(s)
    s_end = n - 1
    def pos_score(i,j):#字符串s中位置(i,j)的分数
        nl=1
        nr=0
        for m in range(i+1,j+1):
            if s[m]=='(':
                nl+=1
            else:
                nr+=1
            if nl==nr:
                new_end=i+2*nr-1 #new_end 匹配的右括号位置
                if i+1==new_end==j:
                    return 1
                elif i+1==new_end:
                    return 1+pos_score(new_end+1,j)
                elif j==new_end:
                    return 2*pos_score(i+1,new_end-1)
                else:
                    return 2*pos_score(i+1,new_end-1)+pos_score(new_end+1,j)
    return pos_score(s_start,s_end)
print(score(s))
#1 2 4 8 16 32 64 128 256

