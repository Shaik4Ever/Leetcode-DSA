class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        averages=[]
        left=0
        right=len(nums)-1
        nums.sort()
        while left<right:
            avg=(nums[left]+nums[right])/2
            averages.append(avg)
            left+=1
            right-=1
        return min(averages)
            