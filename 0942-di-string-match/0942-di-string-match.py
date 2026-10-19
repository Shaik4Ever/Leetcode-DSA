class Solution:
    def diStringMatch(self, s: str) -> list[int]:
        left=0
        right=len(s)
        res=[]
        for i in range(len(s)):
            if s[i]=='I':
                res.append(left)
                left+=1
            else:
                res.append(right)
                right-=1
        res.append(left)
        return res
