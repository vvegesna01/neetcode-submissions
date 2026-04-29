class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        repeated = set()
        l = 0
        longest = 0
        
        for r in range(len(s)):
            while s[r] in repeated:
                repeated.remove(s[l])
                l += 1
        
            repeated.add(s[r])
            
            length = (r - l) + 1
            longest = max(length, longest)
        
        return longest