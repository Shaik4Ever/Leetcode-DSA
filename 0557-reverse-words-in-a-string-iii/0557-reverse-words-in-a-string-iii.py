class Solution:
    def reverseWords(self, s: str) -> str:
        words=s.split()
        new=""
        for i in range(len(words)):
            if i==len(words)-1:
                new+=words[i][::-1]+""
            else:
                new+=words[i][::-1]+" "

            
        return new


        