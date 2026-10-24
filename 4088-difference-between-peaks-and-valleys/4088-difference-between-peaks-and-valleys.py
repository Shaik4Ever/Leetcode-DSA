class Solution:
    def peakValleyDifference(self, nums: list[int]) -> int:
        peaks=0
        valleys=0
        
        for i in range(len(nums)):
            if i==0:
                continue
            elif i==len(nums)-1:
                continue
            else:
                if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                    peaks+=nums[i]
                elif nums[i]<nums[i-1] and nums[i]<nums[i+1]:
                    valleys+=nums[i]
        return peaks-valleys