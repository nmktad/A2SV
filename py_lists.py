if __name__ == '__main__':
    N = int(input())
    _list = []
    
    for _ in range(N):
        action = input().split()
        command = action[0]
        
        if command == 'print':
            print(_list)
        elif command == 'sort':
            _list.sort()
        elif command == 'pop':
            _list.pop()
        elif command == 'reverse':
            _list.reverse()
        elif command == 'insert':
            _list.insert(int(action[1]), int(action[2]))
        elif command == 'remove':
            _list.remove(int(action[1]))
        elif command == 'append':
            _list.append(int(action[1]))
        