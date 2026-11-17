class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        left=0
        right=len(nums)-1
        swap=0
        while left<right:
            while left<right and  nums[right]==0:
                right-=1
            if nums[left]==0 and nums[right]!=0:
                nums[left],nums[right]=nums[right],nums[left]
                swap+=1

                left+=1
                right-=1
            else:
                left+=1
        return swap
        