class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0] * (n+1)
        for num in range(n+1):
            output[num] = output[num >> 1] +(num & 1)

        return output