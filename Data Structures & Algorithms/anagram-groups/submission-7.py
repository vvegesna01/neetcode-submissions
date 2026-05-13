class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)

        for word in strs:
            word_map = [0] * 26
            for c in word:
                word_map[ord(c) - ord('a')] += 1

            output[tuple(word_map)].append(word)
        
        return list(output.values())