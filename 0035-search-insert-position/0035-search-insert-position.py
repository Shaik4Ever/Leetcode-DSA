class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        # ans=0
        for i in range(len(nums)):
            if nums[i]>=target:
                return i
        return len(nums)
        