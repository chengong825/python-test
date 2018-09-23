# class Solution:
#     def findReplaceString(self, S, indexes, sources, targets):
#         """
#         :type S: str
#         :type indexes: List[int]
#         :type sources: List[str]
#         :type targets: List[str]
#         :rtype: str
#         """
#         length=len(indexes)
#         i=0
#         while i<length:
#             t=[]
#             while sources[i] in S:
#                 t.append(S.find(sources[i]))
#             for x in t:
#                 if x==indexes[i]:
#                     S.replace(sources[i],targets[i])



#
# class Solution:
#     def findReplaceString(self, S, indexes, sources, targets):
#         """
#         :type S: str
#         :type indexes: List[int]
#         :type sources: List[str]
#         :type targets: List[str]
#         :rtype: str
#         """
#         length=len(indexes)
#         i=0
#         while i<length:
#
#             if indexes[i]==S.find(sources[i],indexes[i],len(S)):
#                 b=S.replace(sources[i],targets[i],1)
#                 S=b
#             i+=1

print(ord('a'))
