class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        ind=[]
        ans=[]
        count=0
        for i in range(len(s)):
            if s[i]==c:
                ind.append(i)
        for i in range(len(s)):
            if s[i]==c:
                ans.append(0)
                count+=1
            else:
                ans.append(min(abs(x - i) for x in ind))
        return ans

                