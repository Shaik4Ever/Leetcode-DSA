class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:

        # nums.sort()
        # res=[]
        # for i in nums:
        #     if i%k==0 and i not in res:
        #         res.append(i)
        # if not res or res[0] != k:
        #     return k
        # for i in range(len(res)-1):
        #     if res[i+1]!=res[i]+k:
        #         return res[i]+k
        # return res[-1]+k


        s=set(nums)

        ans=k

        while ans in s:
            ans+=k
        return ans
        