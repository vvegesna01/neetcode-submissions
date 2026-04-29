class Solution:
    def isValid(self, s: str) -> bool:
        openClose = {"}" : "{", "]" : "[", ")" : "("}

        stack = []
        for c in s:
            if c in openClose:
                if stack == []:
                    return False
                corr_open = openClose[c]
                corr_bracket = stack.pop()
                if corr_bracket != corr_open:
                    return False
            else:
                stack.append(c)

        return not stack