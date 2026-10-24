class Solution:
    def maxScore(self, s: str) -> int:
        # ans=float('-inf')
        # for i in range(1,len(s)):
        #     left=s[:i]
        #     right=s[i:]
        #     score=left.count('0')+right.count('1')
        #     ans=max(ans,score)
        # return ans


        ans=float('-inf')
        ones=s.count('1')
        zeroes=0
        
        for i in range(len(s)-1):
            if s[i]=='0':
                zeroes+=1
            else:
                ones-=1
            ans=max(ans,zeroes+ones)
        return ans
            

        