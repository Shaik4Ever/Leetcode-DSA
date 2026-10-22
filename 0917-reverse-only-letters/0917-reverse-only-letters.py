class Solution:
    def reverseOnlyLetters(self, s: str) -> str:

        left=0
        right=len(s)-1
        l=list(s)
        while left<right:
            while left<right and not s[left].isalpha():
                left+=1

            while left<right and not s[right].isalpha():
                right-=1

            l[left],l[right]=l[right],l[left]
            left+=1
            right-=1
        return "".join(l)