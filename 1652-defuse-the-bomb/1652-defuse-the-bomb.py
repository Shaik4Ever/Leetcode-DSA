class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        n=len(code)
        res=[]
        if k>0:
            code=code*2
            for i in range(n):
                res.append(sum(code[i+1:k+i+1]))
            return res
        elif k<0:
            code=code*2
            for i in range(n):
                res.append(sum(code[n+k+i:n+i]))
            return res
        else:

            return [0]*n       