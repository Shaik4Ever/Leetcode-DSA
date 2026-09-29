class Solution:
    def maxArea(self, height: List[int]) -> int:
        # #Brute Force
        # # l=[]
        # # for i in range(0,len(height)-1):
        # #     count=1
        # #     for j in range(i+1,len(height)):
        # #         num1=height[i]
        # #         num2=height[j]
        # #         k=min(num1,num2)
        # #         l.append(k*count)
        # #         count+=1
        # # return max(l)

        # #Optimal
        # area=0
        # l=0
        # r=len(height)-1
        # while l<r: #or l!=r
        #     m=min(height[l],height[r])
        #     area=max(area,m*(r-l))
        #     if height[l]<height[r]:
        #         l+=1
        #     else:#Even if height[l]>=height[r]
        #         r-=1
        # return area

        ans=0
        left=0
        right=len(height)-1
        while left<right:
            res=(right-left)*min(height[right],height[left])
            ans=max(ans,res)
            if height[left]<=height[right]:
                left+=1
            else:
                right-=1
        return ans













