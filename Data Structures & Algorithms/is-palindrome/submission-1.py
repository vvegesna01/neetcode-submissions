class Solution:
    def isPalindrome(self, s: str) -> bool:

        # remove non alpha num chars
        alphanum_string = ""
        for c in s:
            if c.isalnum():
                alphanum_string = alphanum_string + c.lower()

        length= len(alphanum_string)
        start = 0
        end = length - 1

        while start < length/2:
            if alphanum_string[start] != alphanum_string[end]:
                return False
            else:
                start += 1
                end -= 1
        return True

        