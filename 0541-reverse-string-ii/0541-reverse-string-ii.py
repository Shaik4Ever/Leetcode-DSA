class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        left=0
        right=len(s)
        new=""
        while left<right:#8<7 fails and we exit 
            new+=s[left:left+k][::-1]#ba,bacdfe
            new+=s[left+k:left+2*k]#bacd,#bacdfeg
            left+=2*k#left=4,8
        return new

        