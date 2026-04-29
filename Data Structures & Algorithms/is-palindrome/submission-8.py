class Solution:
    def isPalindrome(self, s: str) -> bool:
        

        # two pointers method
        temp_str = ""

        # clean up the string
        for c in s:
            if c.isalnum():
                temp_str += c.lower()
        
        l, r = 0, len(temp_str) - 1
        while l < len(temp_str):
            if temp_str[l] != temp_str[r]:
                return False
            else:
                l += 1
                r -= 1
        
        return True