class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        
        count = 0
        
        left = 0
        right = len(people) - 1
        
        while left <= right:
            count += 1

            if people[left] + people[right] <= limit:
                left += 1
            
            right -= 1

        return count