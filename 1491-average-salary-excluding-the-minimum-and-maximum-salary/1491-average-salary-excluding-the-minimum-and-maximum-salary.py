class Solution:
    def average(self, salary: List[int]) -> float:
            salary.sort()
            salary = salary[1:-1]
            
            total = 0
            for sal in salary:
                total += sal
                
            return total/len(salary)
            