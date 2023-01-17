def countSwaps(a):
    counter = 0
    for i in range(n):
        for j in range(n-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                counter += 1
                
    print(f"Array is sorted in {counter} swaps.\nFirst Element: {a[0]} \nLast Element: {a[len(a) - 1]}")