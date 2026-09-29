class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # nums.sort()
        # l=0
        # res=[]
        # while l<len(nums):
        #     if l>0 and nums[l]==nums[l-1]:
        #         l+=1
        #         continue
        #     m=l+1
        #     r=len(nums)-1
        #     while m<r:
        #         total=nums[l]+nums[m]+nums[r]
        #         if total==0:
        #             res.append([nums[l],nums[m],nums[r]])
        #             while m<r and nums[m]==nums[m+1]:
        #                 m+=1
        #             while m<r and nums[r]==nums[r-1]:
        #                 r-=1
        #             m+=1
        #             r-=1
        #         elif total>0:
        #             r-=1
        #         else:
        #             m+=1
        #     l+=1
        # return res

        nums.sort()
        res=[]
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left=i+1
            right=len(nums)-1
            while left<right:
                total=nums[i]+nums[left]+nums[right]
                if total==0:
                    res.append([nums[i],nums[left],nums[right]])
                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    while left<right and nums[right]==nums[right-1]:
                        right-=1
                    left+=1
                    right-=1
                elif total>0:
                    right-=1
                else:
                    left+=1
        return res
        