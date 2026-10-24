class Solution:
    def maxScore(self, s: str) -> int:
        ans=float('-inf')
        for i in range(1,len(s)):
            left=s[:i]
            right=s[i:]
            score=left.count('0')+right.count('1')
            ans=max(ans,score)
        return ans

        