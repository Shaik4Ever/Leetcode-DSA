class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        count=0
        for i in arr1:
            flag=True
            for j in arr2:
                num=abs(i-j)
                if num<=d:
                    flag=False
                    break
            if flag:
                count+=1
        return count
        