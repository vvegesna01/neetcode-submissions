class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {"}": "{", ")": "(", "]": "["}

        stack = []

        for c in s:
            # detected closed bracket
            print(c)
            if c in closeToOpen and stack:
                print("closed detected: ", c)
                if stack[-1] != closeToOpen[c]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)
                print("adding to stack:", stack)
        
        if stack:
            return False
        else:
            return True
                


                
