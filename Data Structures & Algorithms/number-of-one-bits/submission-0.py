class Solution:
    def hammingWeight(self, n: int) -> int:
        i=1
        count=0
        print(1&2)
        for _ in range(32):
            if n&i:
                count+=1
            i*=2
        return count