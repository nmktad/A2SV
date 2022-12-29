# Enter your code here. Read input from STDIN. Print output to STDOUT
len1 = input()
list1 = set(map(int, input().split()))

len2 = input()
list2 = set(map(int, input().split()))

print(len(list1.difference(list2)))