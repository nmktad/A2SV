from collections import defaultdict

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        _dict = defaultdict(int)
        ans = []
        
        for domain in cpdomains:
            [count, domain] = domain.split()
            domain = domain.split('.')
                        
            for i, extension in enumerate(domain):
                if len(domain) == 2:
                    if i == 0:
                        _dict[f"{extension}.{domain[1]}"] += int(count)
                    elif i == 1:
                        _dict[extension] += int(count)
                elif len(domain) == 3:
                    if i == 0:
                        _dict[f"{extension}.{domain[1]}.{domain[2]}"] += int(count)
                    elif i == 1:
                        _dict[f"{extension}.{domain[2]}"] += int(count)
                    elif i == 2:
                        _dict[extension] += int(count)
                        
        for key in _dict:
            ans.append(f"{_dict[key]} {key}")
            
        return ans
            
    