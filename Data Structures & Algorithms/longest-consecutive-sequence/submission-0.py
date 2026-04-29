class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = nums

        longest = 0

        for n in numSet:
            #check if n is start of sequence (no left neighbour)
            if (n-1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                    longest = max(longest, length)
                
        return longest