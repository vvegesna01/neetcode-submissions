class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # given nums
        # return len of longestConsecutiveSequence

        # starts of sequences don't have left neighbour
        numsSet = set(nums)
        longest = 0
        for num in nums:
            # check if start of sequence
            if num-1 not in nums:
                length = 0
                while (num + length) in numsSet:
                    length += 1
                longest = max(length, longest)
        
        return longest


