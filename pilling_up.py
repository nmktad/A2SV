# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
for testcase in range(T):    
    n = int(input())
    blocks = [int(x) for x in input().split()]

    l_pointer = 0
    r_pointer = n - 1
    
    stack = []
    
    while l_pointer <= r_pointer:
        max_val = max(blocks[l_pointer], blocks[r_pointer])
        stack.append(max_val)
        
        if max_val == blocks[r_pointer]:
            r_pointer -= 1  
        else: 
            l_pointer += 1
    
    if stack == sorted(stack, reverse = True):
        print("Yes")
    else: 
        print("No")
