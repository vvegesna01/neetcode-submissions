

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams_dict = defaultdict(list)
        # n
        for s in strs:
            count = [0] * 26
            # m
            for c in s:
                # getting index of the corresponding letter and adding one to it
                count[ord(c) - ord('a')] += 1


            key = tuple(count)
            anagrams_dict[key].append(s)

        return anagrams_dict.values()


# Time: O(n * m)  
# Space: O(n * m)

            
            
        