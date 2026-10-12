class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        res=[]
        for i in image:
            i.reverse()
            k=i
            left=0
            right=len(k)-1
            while left<=right:
                if k[left]==0:
                    k[left]=1
                else:
                    k[left]=0
                left+=1
                if left<right:
                    if k[right]==0:
                        k[right]=1
                    else:
                        k[right]=0

                    right-=1
                
            res.append(k)
        return res
        