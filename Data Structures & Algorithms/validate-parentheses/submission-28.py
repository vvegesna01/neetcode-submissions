class Solution:
    def isValid(self, s: str) -> bool:
        
        closed = {"}": "{", ")": "(", "]": "["}

        stack = []
        for c in s:

            # closed bracket, check stack
            if c in closed:
                print(closed[c])
                if stack and stack[-1] == closed[c]:
                    stack.pop()

                else:
                    return False
                
            # open
            else:
                stack.append(c)

        
        if not stack:
            return True
        else:
            return False

                
