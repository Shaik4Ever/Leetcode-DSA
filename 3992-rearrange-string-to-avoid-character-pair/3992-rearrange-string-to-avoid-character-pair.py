class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        t=""
        x_part=""
        l=0
        r=len(s)-1
        while l<=r:
            if l!=r:
                if s[l]==x:
                    x_part+=s[l]
                if s[r]==x:
                    x_part+=s[r]
                l+=1
                r-=1
            else:
                element=s[l]
                if element==x:
                    x_part+=element
                l+=1
                
        # return x_part
        y_part=""
        l=0
        r=len(s)-1
        while l<=r:
            if l!=r:
                if s[l]==y:
                    y_part+=s[l]
                if s[r]==y:
                    y_part+=s[r]
                l+=1
                r-=1
            else:
                element=s[l]
                if element==y:
                    y_part+=element
                l+=1
        # return y_part
        

        other=""
        l=0
        r=len(s)-1
        while l<=r:
            if l!=r:
                if s[l]!=x and s[l]!=y:
                    other+=s[l]
                if s[r]!=x and s[r]!=y:
                    other+=s[r]
                l+=1
                r-=1
            else:
                element=s[l]
                if element !=x and element !=y:
                    other+=element
                l+=1
        # return other
        return y_part+other+x_part