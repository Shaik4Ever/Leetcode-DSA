class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        # n=len(nums)
        # half=n//2
        # if nums[0]%2==0:
        #     even=nums[:half]
        #     odd=nums[half:]
        # else:
        #     odd=nums[:half]
        #     even=nums[half:]


        # res=[]
        # even_index=0
        # odd_index=0
        # for i in range(n):
        #     if i%2==0:
        #         res.append(even[even_index]) 
        #         even_index+=1
        #     else:
        #         res.append(odd[odd_index])
        #         odd_index+=1
        # return res
        even=[]
        odd=[]
        for i in nums:
            if i%2==0:
                even.append(i)
            else:
                odd.append(i)
        res=[]
        even_index=0
        odd_index=0
        for i in range(len(nums)):
            if i%2==0:
                res.append(even[even_index])
                even_index+=1
            else:
                res.append(odd[odd_index])
                odd_index+=1
        return res