class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        repeatedSet = set()
        l = 0
        max_len = 0
        for r in range(len(s)):
            #if duplicate char, update window and set
            while s[r] in repeatedSet:
                repeatedSet.remove(s[l])
                l += 1
            repeatedSet.add(s[r])
            max_len = max(max_len, (r - l + 1))
        return max_len
                

            


        