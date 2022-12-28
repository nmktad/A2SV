class Solution:
    def multiply(self, num1: str, num2: str) -> str:    
        def getNo(num, i): 
            return num // 10 ** i % 10
        
        ptr1 = len(num1) - 1       
        carry = 0
        totalSum = 0
        
        ans = []
        
        while ptr1 >= 0:
            ptr2 = len(num2) - 1
            
            temp_ans = ""
            
            while ptr2 >= 0:
                temp = int(num1[ptr1]) * int(num2[ptr2]) + carry
                
                carry = 0
                
        
                if ptr2 != 0:
                
                    if temp > 9:
                        temp_ans += str(getNo(temp, 0))
                        carry = getNo(temp, 1)
                    else:
                        temp_ans += str(temp)

                    print(f"answer for {num2[ptr2]} and {num1[ptr1]} is {temp_ans} with carry of {carry}")

                else:
                    temp_ans += str(temp)[::-1]
                    
                ptr2 -= 1
            
            ans.append(temp_ans[::-1])
            print("\n")
            
            ptr1 -= 1
            
        print(ans)
            
        for i in range(len(ans) - 1, -1, -1):
            ans[i] += '0' * i
            
            totalSum += int(ans[i])
        
        print(ans)
        return str(totalSum)
        
            
        