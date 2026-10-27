class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        s=set(arr)
        for i in arr:
            if i!=0 and i*2 in s:
                return True
        if arr.count(0)>=2:
            return True
        return False
        
        