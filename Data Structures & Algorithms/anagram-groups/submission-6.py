class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)
        for string in strs:
            freq_str = [0] * 26
            for c in string:
                freq_str[ord(c) - ord('a')] += 1
            
            res[tuple(freq_str)].append(string)
        
        print(res)
        return list(res.values())

