class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        ans = []
        groups = defaultdict(list)
        
        for txn in transactions:
            name, time, amount, city = txn.split(",")
            groups[name].append((time, amount, city))
        
        for i in range(len(transactions)):
            name, time, amount, city = transactions[i].split(",")

            if int(amount) > 1000:
                ans.append(transactions[i])
            else:
                for txn in groups[name]:
                    time_i, _, city_i = txn
                    if city != city_i and abs(int(time) - int(time_i)) <= 60:
                        ans.append(transactions[i])
                        break

        return ans