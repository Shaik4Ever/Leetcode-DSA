class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        #Using stack
        
        # r1=[]
        # r2=[]
        # for i in s:
        #     if i=="#" and len(r1)!=0:
        #         r1.pop()
        #     elif i=="#" and len(r1)==0:
        #         continue
        #     else:
        #         r1.append(i)
        # for j in t:
        #     if j=='#' and len(r2)!=0:
        #         r2.pop()
        #     elif j=="#" and len(r2)==0:
        #         continue
        #     else:
        #         r2.append(j)

        # # return r2
        # return r1==r2





        #Using Two Pointers
        right=len(s)-1
        ss=""
        skip=0
        while right>=0:
            if s[right]=="#":
                skip+=1
            elif skip>0:
                skip-=1
            else:
                ss+=s[right]
            right-=1
        ss=ss[::-1]
        # return ss



        right=len(t)-1
        tt=""
        skip=0
        while right>=0:
            if t[right]=="#":
                skip+=1
            elif skip>0:
                skip-=1
            else:
                tt+=t[right]
            right-=1
        tt=tt[::-1]
        # return tt

        return ss==tt        
