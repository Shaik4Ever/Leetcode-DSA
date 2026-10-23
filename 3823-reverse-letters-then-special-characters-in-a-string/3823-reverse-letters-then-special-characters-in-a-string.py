class Solution:
    def reverseByType(self, s: str) -> str:
        lowercaseLeft=0
        lowercaseRight=len(s)-1
        specialLeft=0
        specialRight=len(s)-1
        
        new=list(s)

        while lowercaseLeft<lowercaseRight:
            while lowercaseLeft<lowercaseRight and not s[lowercaseLeft].isalpha():
                lowercaseLeft+=1
            while lowercaseLeft<lowercaseRight and not s[lowercaseRight].isalpha():
                lowercaseRight-=1
            new[lowercaseLeft],new[lowercaseRight]=new[lowercaseRight],new[lowercaseLeft]
            lowercaseLeft+=1
            lowercaseRight-=1
        # return "".join(new)

        while specialLeft<specialRight:
            while specialLeft<specialRight and s[specialLeft].isalpha():
                specialLeft+=1
            while specialLeft<specialRight and s[specialRight].isalpha():
                specialRight-=1
            new[specialLeft],new[specialRight]=new[specialRight],new[specialLeft]
            specialLeft+=1
            specialRight-=1
        return "".join(new)



        
        