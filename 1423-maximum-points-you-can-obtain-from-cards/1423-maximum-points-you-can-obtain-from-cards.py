class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        # left=0
        # right=len(cardPoints)-1
        # k1=k
        # ls=cardPoints[0]
        # while k!=1:
        #     if cardPoints[left+1]>=cardPoints[right]:
        #         ls+=cardPoints[left+1]
        #         left+=1
        #     else:
        #         ls+=cardPoints[right]
        #         right-=1
        #     k-=1
        # # return ls
        # left=0
        # right=len(cardPoints)-1
        # rs=cardPoints[right]
        # while k1!=1:
        #     if cardPoints[right-1]>=cardPoints[left]:
        #         rs+=cardPoints[right-1]
        #         right-=1
        #     else:
        #         rs+=cardPoints[left]
        #         left+=1
        #     k1-=1
        # return max(rs,ls)

        currSum=sum(cardPoints[len(cardPoints)-k:])
        # return currSum
        ans=currSum
        for i in range(k):
            currSum+=cardPoints[i]
            currSum-=cardPoints[len(cardPoints)-k+i]

            if currSum>ans:
                ans=currSum
        return ans