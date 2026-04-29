class Solution:
    def isPalindrome(self, s: str) -> bool:

        # remove non alpha num char
        new_s = ""
        for c in s:
            if c.isalnum():
                new_s += c.lower()

        print(new_s)
        

        l, r = 0, len(new_s)-1
        while(l <= r):
            if new_s[l] != new_s[r]:
                return False
            l += 1
            r -= 1
        return True
        