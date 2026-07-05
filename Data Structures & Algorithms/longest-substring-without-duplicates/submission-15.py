class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        longest = 0
        l = 0
        repeated = set()

        for r in range(len(s)):

            print("current char:", s[r])
            while s[r] in repeated:
                print("repeat detected")
                repeated.remove(s[l])
                l += 1
            repeated.add(s[r])

            length = r - l + 1
            print("length:", length)
            longest = max(length, longest)
        
        return longest


