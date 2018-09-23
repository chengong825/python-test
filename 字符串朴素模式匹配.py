class Solution:
    def index(self,S,T):
        s=len(S)
        t=len(T)
        i=0
        j=0
        while i<s and j<t:
            if S[i]==T[j]:
                i+=1
                j+=1
            else:

                i=i-j+1
                j = 0
        if j==t:
            return i-j
        else:
            return -1
    def get_next(self,T):
        next=[-1]
        t=len(T)
        i=0
        j=-1
        while i <t:
            if j==-1 or T[i]==T[j]:
                i+=1
                j+=1
                next.append(j)
            else:
                j=next[j]


        return next
    def KMP_index(self,S,T):
        s=len(S)
        t=len(T)
        i=0
        j=0
        next=self.get_next(T)
        while i < s and j< t:
            if j==0 or S[i]==T[j]:
                j+=1
                i+=1
            else:
                j=next[j]
        if j==t:
            return i-j
        else:
            return -1

solution=Solution()
S='goodgoogle'
T='google'
print(solution.get_next(T))
print(solution.index(S,T))
print(solution.KMP_index(S,T))