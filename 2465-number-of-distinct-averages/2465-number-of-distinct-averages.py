class Solution:
    def distinctAverages(self, nums: list[int]) -> int:
        nums.sort()
        left=0
        right=len(nums)-1
        s=set()
        while left<right:
            avg=(nums[left]+nums[right])/2
            s.add(avg)
            left+=1
            right-=1
        return len(s)
        