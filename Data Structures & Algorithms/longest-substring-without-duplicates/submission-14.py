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
            curr_len = r - l  + 1
            longest = max(longest, curr_len)

        return longest