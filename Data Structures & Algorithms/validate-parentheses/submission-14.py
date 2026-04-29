class Solution:
    def isValid(self, s: str) -> bool:
        
        bracketsMap = {"]": "[", "}": "{", ")": "("}
        stack = []

        for c in s:

            # check if it is an open bracket
            if c not in bracketsMap:
                stack.append(c)
            
            else:
                # check if stack is empty
                if not stack:
                    return False
                
                else:
                    popped = stack.pop()

                    # check if the brackets match
                    if popped != bracketsMap[c]:
                        return False
        
        return not stack