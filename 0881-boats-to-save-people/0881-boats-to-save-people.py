class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        left=0
        right=len(people)-1
        people.sort()
        boat=0
        while left<=right:
            s=people[left]+people[right]

            if s<=limit:
                
                left+=1
                right-=1
            else:
                right-=1

            boat+=1

        return boat