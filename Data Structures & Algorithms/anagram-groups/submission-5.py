class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)
        for string in strs:
            mapped = [0] * 26

            for c in string:
                mapped[ord(c) - ord('a')] += 1
            
            key = tuple(mapped)
            res[key].append(string)
        
        return list(res.values())