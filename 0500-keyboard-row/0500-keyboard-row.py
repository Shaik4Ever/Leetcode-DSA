class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        fr="qwertyuiop"
        sr="asdfghjkl"
        tr="zxcvbnm"

        ans=[]
        for i in words:
            word=i.lower()
            if(all(ch in fr for ch in word) or all(ch in sr for ch in word) or all(ch in tr for ch in word)):
                ans.append(i)
        return ans 
