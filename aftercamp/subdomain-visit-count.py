class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        ht = defaultdict(int)

        for domain in cpdomains:
            count, domain = domain.split()

            pos = domain.find('.')

            while pos != -1:
                ht[domain] += int(count)
                domain = domain[pos+1:]
                pos = domain.find('.')

            ht[domain] += int(count)

        return [str(count) + " " + key for key, count in ht.items()]