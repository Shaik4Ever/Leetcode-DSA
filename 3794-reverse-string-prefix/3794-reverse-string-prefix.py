class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        last=s[k:]
        # left=0
        right=k-1
        first=""
        while right>=0:
            first+=s[right]
            right-=1

        return first+last
        