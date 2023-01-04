[a, b, c] = map(int, input().split())
 
if a > b:
    print((2 * b) + 1 + (2 * c))
elif a == b:
    print(2 * a + (2 * c))
else:
    print((2 * a) + 1 + (2 * c))
