class Solution:
    def countSubstrings(self, s: str) -> int:
        # ans=0
        # for i in range(len(s)):
        #     left=i
        #     right=len(s)
        #     while left<=right:
        #         if s[left:right]==s[left:right][::-1]:#[abc][cba],
        #             ans+=1
        #         left+=1
        #         right-=1
        # return ans
            #[aaa][a][aa][a][a]

        #Above solutioin is not gonna work
        ans=0
        for i in range(len(s)):
            left=i
            right=i+1
            while right<=len(s):
                if s[left:right]==s[left:right][::-1]:
                    ans+=1
                right+=1
        return ans