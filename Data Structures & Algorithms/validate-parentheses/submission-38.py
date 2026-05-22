class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {"}": "{", "]": "[", ")": "("}

        stack = []
        for c in s:
            # closed bracket 
            if c in closeToOpen.keys():
                print("in dict:", closeToOpen[c])

                if not stack:
                    return False
                if stack and closeToOpen[c] != stack[-1]:
                    return False
                else:
                    stack.pop()

            # open bracket
            else:
                stack.append(c)
        
        if stack:
            return False
        if not stack:
            return True
