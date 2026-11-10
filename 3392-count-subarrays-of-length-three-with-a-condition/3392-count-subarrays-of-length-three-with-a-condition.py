class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        sub_arrays=[]
        for i in range(len(nums)-2):
            sub_arrays.append(nums[i:i+3])
        ans=0
        for i in sub_arrays:
            if i[0]+i[-1]==i[1]/2:
                ans+=1
        return ans


