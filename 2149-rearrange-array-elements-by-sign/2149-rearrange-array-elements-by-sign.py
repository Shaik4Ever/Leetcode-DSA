class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        p=[]
        n=[]
        ans=[]
        for i in nums:
            if i>=0:
                p.append(i)
            else:
                n.append(i)
        for i in range(len(p)):
            ans.append(p[i])
            ans.append(n[i])
        return ans




        