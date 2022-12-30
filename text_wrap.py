import textwrap

def wrap(string, max_width):
    ans = ''
    for i in range(len(string)):
        if i!=0 and i % max_width == 0:
            ans+="\n"
        ans+=string[i]    
    return ans

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)