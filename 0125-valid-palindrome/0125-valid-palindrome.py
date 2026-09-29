class Solution:
    def isPalindrome(self, s: str) -> bool:
        #This is TC of O(n)

        # s=s.lower()
        # forward=""
        # for i in s:
        #     if i.isalnum():
        #         forward+=i
        # reverse=""
        # for i in range(len(forward)-1,-1,-1):
        #     reverse+=forward[i]
        # if reverse==forward:
        #     return True
        # else:
        #     return False

        #Two Pointers
        # new_s="".join(i.lower() for i in s if i.isalnum())
        # left=0
        # right=len(new_s)-1
        # while left<right:
        #     if new_s[left]!=new_s[right]:
        #         return False
        #     left+=1
        #     right-=1
        # return True

        #Using Slicing
        # new_s="".join(c.lower() for c in s if c.isalnum())
        # return new_s==new_s[::-1]


        new_s="".join(i.lower() for i in s if i.isalnum())
        left=0
        right=len(new_s)-1
        while left<right:
            if new_s[left]!=new_s[right]:
                return False
            left+=1
            right-=1
        return True
