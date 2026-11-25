from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        new=paragraph.lower()
        final=""
        for i in new:
            if i.isalpha() or i==" ":
                final+=i
            else:
                final+=" "
        # return final        
        c=Counter(final.split())
        for k,v in c.items():
            if k in banned:
                c[k]=0
        # return c
        m=float('-inf')
        ans=""
        for k,v in c.items():
            if v>m:
                ans=k
                m=max(m,v)
        return ans