class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        index=1
        prev=nums[0]
        for i in range(1,len(nums)):
            if nums[i]==prev:
                continue
            else:
                prev=nums[i]
                nums[index]=prev
                index+=1
        return index