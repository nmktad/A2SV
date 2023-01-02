input_no = int(input())
 
for _ in range(input_no):
    word = input()
    stuttered_word = ""
    
    for i in range(2):
        stuttered_word += word[i]
    
    stuttered_word += '... '
    stuttered_word += word + "?"
    
    print(stuttered_word)
