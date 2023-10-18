class Solution:
    def calculate(self, s: str) -> int:
        def applyOp(a, b, op):
            if op == '+': return a + b
            if op == '-': return a - b
            if op == '*': return a * b
            if op == '/': return a // b

        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

        values = []
        ops = []
        i = 0
        
        while i < len(s):
            if s[i] == " ":
                i+=1
                continue

            if s[i].isdigit():
                val = 0
                
                while (i < len(s) and s[i].isdigit()):
                    val = (val * 10) + int(s[i])
                    i += 1
                
                values.append(val)
                i-=1
            else:
                while ops and precedence[ops[-1]] >= precedence[s[i]]:
                    val2 = values.pop()
                    val1 = values.pop()
                    op = ops.pop()
                    
                    values.append(applyOp(val1, val2, op))
                ops.append(s[i])
            
            i += 1

        while len(ops) != 0:
            val2 = values.pop()
            val1 = values.pop()
            op = ops.pop()
                    
            values.append(applyOp(val1, val2, op))

        return values[-1]