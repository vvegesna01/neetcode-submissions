class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 0  1.  2. 3  4. 5
        #[-1, 0, 2, 4, 6, 8]
        # l      m.       r
        index = -1

        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (r + l) // 2

            if nums[mid] == target:
                return mid

            # target on the right
            if target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
            
        return index
