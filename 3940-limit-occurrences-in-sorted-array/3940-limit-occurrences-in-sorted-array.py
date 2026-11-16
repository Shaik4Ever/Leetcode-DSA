from collections import Counter
class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        c=Counter(nums)
        res=[]
        for key,val in c.items():
            if val>k:
                for j in range(k):
                    res.append(key)
            else:
                for j in range(val):
                    res.append(key)
        

        return res