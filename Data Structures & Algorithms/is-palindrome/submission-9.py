class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        
        checked_s = ""
        for c in s:
            if c.isalnum():
                checked_s += c.lower()
        l = 0
        r = len(checked_s) - 1

        while l <= r:
            if checked_s[l] != checked_s[r]:
                return False
            else:
                l += 1
                r -= 1
        return True
        