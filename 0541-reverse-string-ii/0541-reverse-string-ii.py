class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        left=0
        right=len(s)
        new=""
        while left<right:
            new+=s[left:left+k][::-1]
            new+=s[left+k:left+2*k]
            left+=2*k
        return new

        