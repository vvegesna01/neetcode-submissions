class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        closedBrackets = {"}": "{", ")": "(", "]": "["}

        if len(s) < 2:
            return False

        for c in s:
            if c in closedBrackets:
                if stack and stack[-1] == closedBrackets[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        
        return True if not stack else False
        