class Solution:
    def scoreBalance(self, s: str) -> bool:
        total=0
        for i in s:
            total+=(ord(i)-ord('a')+1)
        # return total
        till=0
        for i in s:
            k=ord(i)-ord('a')+1
            till+=k
            if till==total-till:
                return True
        return False