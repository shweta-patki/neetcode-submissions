class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        m = max(nums)
        summ = m*(m+1)/2
        missing = int(summ-sum(nums))
        if missing==0 and 0 in nums:
            return m+1
        return missing