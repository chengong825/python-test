# 给定两个句子 A 和 B 。 （句子是一串由空格分隔的单词。每个单词仅由小写字母组成。）
#
# 如果一个单词在其中一个句子中只出现一次，在另一个句子中却没有出现，那么这个单词就是不常见的。
#
# 返回所有不常用单词的列表。
#
# 您可以按任何顺序返回列表。
# 示例 1：
#
# 输入：A = "this apple is sweet", B = "this apple is sour"
# 输出：["sweet","sour"]
# 示例 2：
#
# 输入：A = "apple apple", B = "banana"
# 输出：["banana"]
st1='asds sad'
st2='kjnjk asd sad'
s1=st1.split()
s2=st2.split()
res=[]
for i in st1:
    if i not in s2 and s1.count(i)==1:
        res.append(i)
for j in st2:
    if j not in s1 and s2.count(j)==1:
        res.append(j)

class Solution(object):
    def uncommonFromSentences(self, A, B):
        count = {}
        for word in A.split():
            count[word] = count.get(word, 0) + 1
        for word in B.split():
            count[word] = count.get(word, 0) + 1

        #Alternatively:
        #count = collections.Counter(A.split())
        #count += collections.Counter(B.split())

        return [word for word in count if count[word] == 1]