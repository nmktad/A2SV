for _ in range(int(input())):
    n=int(input())
    
    nums=list(map(int,input().split()))
    
    right=0
    
    flag= 1 if nums[0] > 0 else 0
    
    sums=0
    
    key=nums[0]
    
    while right < len(nums):
        if flag == 1:
            if nums[right] > 0:
                key=max(key,nums[right])
            else:
                sums+=key
                key=nums[right]
                flag=0
        else:
            if nums[right] < 0:
                key=max(key,nums[right])
            else:
                sums+=key
                key=nums[right]
                flag=1
        
        right += 1
        
    sums += key
    print(sums)
