class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        # fr= "".join(sorted("qwertyuiop"))
        # sr= "".join(sorted("asdfghjkl"))
        # tr= "".join(sorted("zxcvbnm"))
        # ans=[]
        # for i in words:
        #     i=set(i)
        #     if "".join(sorted(i)) in fr or "".join(sorted(i)) in sr or "".join(sorted(i)) in tr:
        #         ans.append("".join(sorted(i)))
        # return ans

        fr="qwertyuiop"
        sr="asdfghjkl"
        tr="zxcvbnm"

        ans=[]
        for i in words:
            word=i.lower()
            if(all(ch in fr for ch in word) or all(ch in sr for ch in word) or all(ch in tr for ch in word)):
                ans.append(i)
        return ans 
