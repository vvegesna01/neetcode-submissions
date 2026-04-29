class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        maxString = 0
        charSet = set()
        l = 0
        for r in range(len(s)):
            while s[r] in charSet:
                # remove leftmost to make sure window is valid
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            maxString = max(maxString, r - l + 1)
        return maxString
