class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # j=0
        # for i in range(len(nums)):
        #     if nums[i]!=0:
        #         nums[j],nums[i]=nums[i],nums[j]
        #         j+=1
        # prev=0
        # j=0
        # while j<=len(nums)-1:
        #         if nums[j]!=0:
        #             nums[j],nums[prev]=nums[prev],nums[j]
        #             prev+=1
        #         j+=1

        # i=0
        # j=1
        # k=len(nums)
        # while i<j and j!=k:
        #     if nums[i]==0 and nums[j]==0:
        #         j+=1
        #     elif nums[i]==0:
        #         nums[i],nums[j]=nums[j],nums[i]
        #         i+=1
        #         j+=1
        #     else:
        #         i+=1
        #         j+=1
        # return nums
        

        
                 
        # i=0
        # j=1

        # def swap(start:int,end:int)->None:
        #     nums[start],nums[end]=nums[end],nums[start]
        # while i<j and j!=len(nums):
        #     if nums[i]==0 and nums[j]!=0:
        #         swap(i,j)
        #         i+=1
        #         j+=1
        #     elif nums[i]==0 and nums[j]==0:
        #         j+=1
        #     else:
        #         i+=1
        #         j+=1
        # return nums


        # i=0
        # j=1
        # while j!=len(nums):
        #     if nums[i]==0 and nums[j]==0:
        #         j+=1
        #     elif nums[i]==0:
        #         nums[i],nums[j]=nums[j],nums[i]
        #         i+=1
        #         j+=1
        #     else:
        #         i+=1
        #         j+=1
        # return nums

        l=0
        r=1
        while r<len(nums):
            # while nums[l]!=0:
            #     l+=1
            # while nums[r]>0:
            #     r+=1
            # nums[l],nums[r]=nums[r],nums[l]
            if nums[l]==0 and nums[r]!=0:
                nums[l],nums[r]=nums[r],nums[l]
            if nums[l]!=0:
                l+=1
            if nums[r]==0:
                r+=1
            else:
                r+=1
        return nums


            
