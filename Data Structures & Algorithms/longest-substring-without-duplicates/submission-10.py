class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # given s
        # return len of longest substr
        # no repeating characters

        longest = 0
        #z[xyz]xyz
        repeated = set()
        l = 0

        for r in range(len(s)):
            while s[r] in repeated:
                repeated.remove(s[l])
                l += 1
            else:
                repeated.add(s[r])
                length = r - l + 1
                longest = max(length, longest)
                
        
        return longest


                    