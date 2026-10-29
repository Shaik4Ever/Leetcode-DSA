class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        count=0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                arr=nums[:i]+nums[j+1:]
                if all(arr[k]<arr[k+1] for k in range(len(arr)-1)):
                    count+=1
        return count