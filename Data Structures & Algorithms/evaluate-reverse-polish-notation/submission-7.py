class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        ops = ["*", "+", "-", "/"]
        stack = []
        result = 0
        for token in tokens:
            
            if token in ops:
                print("op detected")
                v2 = int(stack.pop())
                v1 = int(stack.pop())
                if token == "+":
                    result = v1 + v2
                elif token == "-":
                    result = v1 - v2
                elif token == "/":
                    result = v1 / v2
                else:
                    result = v1 * v2
                
                stack.append(result)
                print(stack)
            else:
                print("append num")
                print(stack)
                stack.append(token)
        print(stack)
        return int(stack[-1])
