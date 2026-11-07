from collections import Counter
class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:

        # n=len(nums)
        # n=n//2

        # c=Counter(nums)
        # for k,v in c.items():
        #     if v==n:
        #         return k


        s=set()
        for i in nums:
            if i in s:
                return i
            else:
                s.add(i)

        