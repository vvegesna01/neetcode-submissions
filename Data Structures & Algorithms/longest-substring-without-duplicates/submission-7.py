class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        repeatedChars = []

        # zxyzxy
        l = 0 
        longest = 0
        for r in range(len(s)):
            length = 0
            while s[r] in repeatedChars:
                repeatedChars.remove(s[l])
                l += 1
                # making sure window is unique
            repeatedChars.append(s[r])
            length = r - l + 1
            longest = max(length, longest)
        
        return longest

