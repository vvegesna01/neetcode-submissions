class Solution:
    def isValid(self, s: str) -> bool:

        closeBrackets = {"}": "{", "]": "[", ")": "("}
        stack = []
        for c in s:
            if c in closeBrackets.values():
                stack.append(c)
            elif c in closeBrackets:
                if stack == []:
                    return False
                lastChar = stack.pop()
                if lastChar != closeBrackets[c]:
                    return False
                    
        return not stack
        