class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        curr = 1
        for i in range(n):
            prefix[i] = curr
            curr *= nums[i]
        curr = 1
        for j in range(n - 1, -1, -1):
            suffix[j] = curr
            curr *= nums[j]
        return [prefix[i] * suffix[i] for i in range(n)]
