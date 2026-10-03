class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:

        #Wrong method
        # gi=0
        # si=0
        # G=set(g)
        # count=0
        # for si in s:
        #     # if gi<len(g) and si>=g[gi] :
        #     #     count+=1
        #     #     gi+=1

        #     if si in G:
        #         count+=1
        #         G.discard(si)
            
        # return count

        g.sort()
        s.sort()
        gi=0
        count=0
        for cookie in s:
            if gi<len(g) and cookie>=g[gi]:
                gi+=1
                count+=1


        return count