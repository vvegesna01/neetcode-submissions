class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
            
        alpha_s = 26 * [0]
        alpha_t = 26 * [0]


        for c in s: 
            alpha_s[ord(c)-ord('a')] += 1
        for c in t:
            alpha_t[ord(c)-ord('a')] += 1

        if alpha_s == alpha_t:
            return True
        return False