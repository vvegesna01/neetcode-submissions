class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        temp_s = ""
        for c in s:
            if c.isalnum():
                temp_s += c.lower()
        

        start = 0
        end = len(temp_s) - 1
        

        print(temp_s)
        while start < end:
            if temp_s[start] != temp_s[end]:
                return False
            start += 1
            end -=1 
        return True
