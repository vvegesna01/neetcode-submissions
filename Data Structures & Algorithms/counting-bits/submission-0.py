class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0] * (n+1)
        pos = 1
        for i in range(1, n+1):
            print("i:", i)
            count = 0
            while i > 0:
                i = i & (i - 1)
                count += 1
            print("count:", count)
            output[pos] = count
            pos += 1
        
        return output
