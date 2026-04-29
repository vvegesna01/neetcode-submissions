class Solution:
    def isValid(self, s: str) -> bool:
        
        bracketsMap = { ")" : "(", "]" : "[", "}" : "{" }
        stack = []

        for c in s:
            # detect opening bracket, add to stack
            if c not in bracketsMap:
                stack.append(c)
            else:
                #check if stack is empty for closing bracket
                if not stack:
                    return False
                #check if corresponding "popped" bracket matches current closing bracket
                popped = stack.pop()
                if popped != bracketsMap[c]:
                    return False
        
        # check if stack is empty
        return not stack
                
