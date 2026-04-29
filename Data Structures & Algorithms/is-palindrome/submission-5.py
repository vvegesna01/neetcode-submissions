class Solution:
    def isPalindrome(self, s: str) -> bool:

        # remove non alpha characters
        new_s = ""
        for c in s:
            if c.isalnum():
                new_s += c.lower()

        l, r = 0, len(new_s) -1 
        print(new_s)
        while r > l:
            print("left ptr: ", new_s[l])
            print("right ptr: ", new_s[r])
            if new_s[l] != new_s[r]:
                return False
            else:
                l += 1
                r -= 1
        
        return True


        