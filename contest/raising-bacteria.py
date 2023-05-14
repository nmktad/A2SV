n = int(input())
 
count = 0
 
while n > 2:
    count += n % 2
    n //= 2
 
print(count+1)