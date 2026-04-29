class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #sort the strings
        new_s = sorted(s)
        new_t = sorted(t)

        #check if strings are the same
        if new_s == new_t:
            return True

        return False
        