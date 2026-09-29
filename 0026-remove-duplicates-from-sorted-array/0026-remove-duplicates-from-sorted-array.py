class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # l=[]
        # for i in nums:
        #     if i not in l:
        #         l.append(i)
        # k=len(l)
        # # for i in range(len(nums)-k):
        # #     l.append('@')
        # # return k
        # for i in range(k):
        #     nums[i]=l[i]
        # return k

        # # j=0
        # # for i in range(len(nums)):
        # #     if nums[i]!=nums[j]:
        # #         j+=1
        # #         nums[j]=nums[i]
        # # return j+1
        

        slow=0
        fast=1
        count=1
        index=1
        while fast<len(nums):
            if nums[slow]==nums[fast]:
                fast+=1
            else:
                count+=1
                nums[index]=nums[fast]
                index+=1
                slow=fast
                fast+=1
        return count



