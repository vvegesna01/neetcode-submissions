class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {"+":"+", "-":"-", "/":"/", "*":"*"}

        stack = []
        final_val = 0

        for t in tokens:
            # invalid
            if not stack and t in ops:
                return -1
            elif t in ops:
                v2 = stack.pop()
                v1 = stack.pop()
                if t == "+":
                    final_val = v1 + v2
                elif t == "-":
                    final_val = v1 - v2
                elif t == "/":
                    final_val = int(float(v1) / v2)
                elif t == "*":
                    final_val = v1 * v2
                stack.append(int(final_val))
            else:
                stack.append(int(t))
        
        return stack[0]

