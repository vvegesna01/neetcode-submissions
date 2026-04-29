class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        r = 1

        repeated = set()
        longest = 0

        for r in range(len(s)):
    
            print("curr_string:", s[l:r])
            while s[r] in repeated:
                print("removing:", s[l])
                repeated.remove(s[l])
                l += 1
            repeated.add(s[r])
            length = r - l + 1
            longest = max(longest, length)
        
        return longest



