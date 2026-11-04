class Solution:
    def minMoves(self, nums: List[int]) -> int:
        res=[]
        # nums.sort()
        maxi=max(nums)
        for i in nums:
            res.append(maxi-i)
        return sum(res)
        