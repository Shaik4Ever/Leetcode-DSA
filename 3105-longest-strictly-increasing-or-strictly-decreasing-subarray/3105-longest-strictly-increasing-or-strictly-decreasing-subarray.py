class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans=0
        count=0
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                count+=1
                ans=max(ans,count)
            else:
                count=0
        count=0
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                count+=1
                ans=max(ans,count)
            else:
                count=0
        return ans+1

        