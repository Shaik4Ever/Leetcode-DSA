class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        ans=0
        left=0
        right=len(nums)-1
        while left<=right:
            if left==right:
                ans+=nums[left]
            else:
                # temp=""
                temp=str(nums[left])+str(nums[right])
                ans+=int(temp)
            left+=1
            right-=1
        return ans



        