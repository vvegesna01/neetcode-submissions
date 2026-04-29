class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        repeated = set()
        l = 0
        maxLen = 0

        for r in range(len(s)):

            while s[r] in repeated:
                repeated.remove(s[l])
                l += 1

            repeated.add(s[r])
            currLen = r - l + 1
            maxLen = max(maxLen, currLen)

        return maxLen
            