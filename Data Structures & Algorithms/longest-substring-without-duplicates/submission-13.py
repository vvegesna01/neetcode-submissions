class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        repeated = set()

        longest = 0
        
        l = 0

        for r in range(len(s)):
            
            while s[r] in repeated:
                repeated.remove(s[l])
                l += 1
            repeated.add(s[r])
        
            length = r - l + 1
            longest = max(longest, length)
        
        return longest
