class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        stack = []
        l, r = 0, 0
        maxLen = 0

        for r in range(len(s)):
            currLen = 0
            while s[r] in stack:
                print(stack)
                stack[l] = ""
                l += 1
                
            
            currLen = (r - l + 1)
            maxLen = max(maxLen, currLen)
             
            stack.append(s[r])

        return maxLen

