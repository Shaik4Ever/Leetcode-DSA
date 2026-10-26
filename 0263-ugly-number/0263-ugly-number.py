class Solution:
    def isUgly(self, n: int) -> bool:
        # if n<=0:
        #     return False
        # if n==1:
        #     return True
        # for i in range(n+1):
        #     if i<2:
        #         continue
        #     else:
        #         is_prime=True
        #         for j in range(2,int(i**0.5)+1):
        #             if (i%j)==0:
        #                 is_prime=False
        #                 break
        #             else:
        #                 is_prime=True
        #         if is_prime:
        #             if i!=2 and i!=3 and i!=5:
        #                 if n%i==0:
        #                     return False
        # return True


        if n<=0:
            return False
        for i in [2,3,5]:
            while n%i ==0:
                n=n//i
        return n==1


        