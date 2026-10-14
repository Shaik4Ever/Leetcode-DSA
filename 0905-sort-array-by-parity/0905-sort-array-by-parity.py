class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        first=0
        last=len(nums)-1
        even=[]#[4,2]
        odd=[]#[3,1]

        i=0
        while first<=last:
            if nums[first]%2==0:
                even.append(nums[first])
            else:
                odd.append(nums[first])
            first+=1
            if first<=last:
                if nums[last]%2!=0:
                    odd.append(nums[last])
                else:
                    even.append(nums[last])
                last-=1
        return even+odd


        