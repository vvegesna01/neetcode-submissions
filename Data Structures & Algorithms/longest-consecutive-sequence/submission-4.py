class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # [2, 20, 4, 10, 3, 4, 5]
        # 2, 3, 4, 5,    10,   20

        numsSet = set(nums)
        longest = 0

        for num in numsSet:
            # start of sequence detected
            if num-1 not in numsSet:
                length = 1
                while (num + length) in numsSet:
                    length += 1
                
                longest = max(longest, length)
        
        return longest





