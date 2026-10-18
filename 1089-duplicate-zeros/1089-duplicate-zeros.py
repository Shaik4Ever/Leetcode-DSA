class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """

        # i=0
        # n=len(arr)
        # while i<len(arr):
        #     if arr[i]==0:
        #         k=i+1
        #         arr.insert(k,0)
        #         i=k+1
        #     else:
        #         i+=1
        # new=len(arr)
        # for i in range(new-n):
        #     arr.pop()

        n=len(arr)
        i=0
        while i<n:
            if arr[i]==0:
                arr.insert(i+1,0)
                arr.pop()
                i+=2

            else:
                i+=1


        

        