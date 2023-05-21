class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dic = defaultdict(set)
        
        for i in range(len(accounts)):
            dic[(i,accounts[i][0])] = set(accounts[i][1:])

        rep = {(i,j):(i,j) for i,j in dic}
        
        print(dic)
        def find(x):
            if x == rep[x]: 
                return x

            rep[x] = find(rep[x])
            return rep[x]

        def union(v1,v2):
            r1, r2 = find(v1), find(v2)

            if r1 != r2:
                rep[r1] = r2
        
        for acc1 in dic:
            for acc2 in dic:
                if acc1 != acc2 and acc1[1] == acc2[1]:
                    for email in dic[acc1]:
                        if email in dic[acc2]: 
                            union(acc1,acc2)

        ans = []

        for per in rep:
            dic[find(per)].update(dic[per])

        for name in rep:
            if rep[name] == name:
                arr = [name[1]] + list(sorted(list(dic[name])))
                ans.append(arr)
        return ans