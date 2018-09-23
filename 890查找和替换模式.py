# 输入：words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
# 输出：["mee","aqq"]
# 解释：
# "mee" 与模式匹配，因为存在排列 {a -> m, b -> e, ...}。
# "ccc" 与模式不匹配，因为 {a -> c, b -> c, ...} 不是排列。
# 因为 a 和 b 映射到同一个字母。
class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]  or reverse_rules[pattern[i]]!=pattern
        """

        res = []
        lp = len(pattern)

        for word in words:
            rules = {}
            reverse_rules = {}
            for i in range(lp):
                if word[i] not in rules.keys() and pattern[i] not in reverse_rules.keys():
                    rules[word[i]] = pattern[i]
                    reverse_rules[pattern[i]] = word[i]
                    # rules[pattern[i]]=word[i]

                elif word[i] in rules.keys() and pattern[i] in reverse_rules.keys() and rules[word[i]] == pattern[i] and \
                                reverse_rules[pattern[i]] == word[i]:

                    pass

                else:
                    break
            else:
                res.append(word)
        return res


solution = Solution()
print(solution.findAndReplacePattern(['add', 'ads'], 'abb'))
dic={}
print(getattr(dic,'4'))