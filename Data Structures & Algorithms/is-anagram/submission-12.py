class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        s_mapped = [0] * 26
        t_mapped = [0] * 26

        for c in s:
            s_mapped[ord(c) - ord('a')] += 1

        for c in t:
            t_mapped[ord(c) - ord('a')] += 1
        
        return s_mapped == t_mapped