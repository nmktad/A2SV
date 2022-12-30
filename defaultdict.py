# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

nums = list(map(int, input().split()))
list1 = [input() for i in range(nums[0])]
list2 = [input() for i in range(nums[1])]

dict = defaultdict(list)

for i, char in enumerate(list1):
    dict[char].append(str(i + 1))

for char in list2:
    if dict[char]:
        print(' '.join(dict[char]))
    else:
        print(-1)
    