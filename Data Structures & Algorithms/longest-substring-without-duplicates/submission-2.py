class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        # use a set to keep track of distinct chars
        distinct_chars = set()

        # initialize window ptrs
        l, r = 0, 0

        # intialize output
        max_len = 0
        # iterate through string by moving right ptr
        # check if each new char added to window is in set
        # if char in set, remove char from the start of the window while new char is still in set
        # if char not in set, add to set, calc, maxString, move r forward

        # iterating through the string
        for r in range(len(s)):
            curr_len = 0
            # new char in set
            while s[r] in distinct_chars:
                distinct_chars.remove(s[l])
                l += 1
            if s[r] not in distinct_chars:
                distinct_chars.add(s[r])
                curr_len = r - l + 1

                max_len = max(max_len, curr_len)
        
        return max_len





