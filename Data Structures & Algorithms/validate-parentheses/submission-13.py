class Solution:
    def isValid(self, s: str) -> bool:
        
        # initialize stack
        stack = []

        # create map
        bracketsMap = {"}": "{", ")": "(", "]": "["}

        for c in s:
            if c in bracketsMap:
                if stack and stack[-1] == bracketsMap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        if not stack:
            return True
        else:
            return False
