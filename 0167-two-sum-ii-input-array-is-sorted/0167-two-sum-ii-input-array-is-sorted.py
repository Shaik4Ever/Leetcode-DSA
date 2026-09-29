class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # l=[]
        # for i in range(len(numbers)):
        #     for j in range(i+1,len(numbers)):
        #         if numbers[i]+numbers[j]==target:
        #             l.append(i+1)
        #             l.append(j+1)
        #         else:
        #             pass
        # return l

        #Using hashmap
        # hashmap={}
        # for i,num in enumerate(numbers):
        #     k=target-num
        #     if k not in hashmap:
        #         hashmap[num]=i
        #     else:
        #         return [hashmap[k]+1,i+1]
        # return []

        
       #Two Pointers
    #    l=0
    #    r=len(numbers)-1
    #    while l<r:
    #     total=numbers[l]+numbers[r]
    #     if total==target:
    #         return [l+1,r+1]
    #     elif total>target:
    #         r-=1
    #     else:
    #         l+=1
        l=0
        r=len(numbers)-1
        while l<r:
            t=numbers[l]+numbers[r]
            if target>t:
                l+=1
            elif target<t:
                r-=1
            else:
                return [l+1,r+1]
    


        



