count = 0

for _ in range(int(input())):
    count += input().split().count('1')

print(count//2)