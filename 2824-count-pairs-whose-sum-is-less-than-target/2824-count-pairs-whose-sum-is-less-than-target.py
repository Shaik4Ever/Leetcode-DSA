class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        right=len(nums)-1
        ans=0
        for i in range(len(nums)):
            while right>i:
                s=nums[i]+nums[right]
                right-=1
                if s<target:
                    ans+=1
            right=len(nums)-1
        return ans
            

        