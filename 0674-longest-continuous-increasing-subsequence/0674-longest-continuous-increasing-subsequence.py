class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        ans=1
        count=1
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                count+=1
            else:
                count=1
            ans=max(count,ans)
        return ans
        