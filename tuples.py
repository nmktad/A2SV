if __name__ == '__main__':
    num = input()
    tup = tuple(map(int, input().split()))

    print(hash(tup))

