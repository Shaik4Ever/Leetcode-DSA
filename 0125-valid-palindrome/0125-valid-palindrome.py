class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s=""
        for i in s:
            if i.isalnum():
                new_s+=i.lower()
        # return new_s
        first=0
        end=len(new_s)-1
        while first<end:
            if new_s[first]!=new_s[end]:
                return False
            first+=1
            end-=1
        return True
        
        