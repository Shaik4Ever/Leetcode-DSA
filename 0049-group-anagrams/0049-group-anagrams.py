from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # This Below is BruteForce Approch
        #final=[]
        # visited=set()
        # for i in range(len(strs)):
        #   if strs[i] in visited:
        #     continue
        #   dup=[strs[i]]
        #   visited.add(strs[i])
        #   c1=Counter(strs[i])
        #   for j in range(i+1,len(strs)):
        #     c2=Counter(strs[j])
        #     if c1==c2:
        #       dup.append(strs[j])
        #       visited.add(strs[j])
        #   final.append(dup)
        # return final

        # This is Optimal
        hashmap={}
        for i in strs:
            k="".join(sorted(i))
            if k not in hashmap:
                hashmap[k]=list()
            hashmap[k].append(i)
        final=list(hashmap.values())
        return final


       