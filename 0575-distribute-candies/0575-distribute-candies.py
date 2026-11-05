class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        # if len(set(candyType))==1:
        #     return 1
        # else:
            # ans=0
            n=len(candyType)
            ans=min(len(set(candyType)),n//2)
            return ans