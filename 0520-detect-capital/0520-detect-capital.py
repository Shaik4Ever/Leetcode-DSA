class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        caps=word.upper()
        if word==caps:
            return True
        else:
            firstCap=True
            middleCap=False
            for i in range(len(word)):
                char=word[i].upper()
                if i==0 and word[i]==char:
                    firstCap=True
                else:
                    if word[i]==char:
                        return False
            return True
        