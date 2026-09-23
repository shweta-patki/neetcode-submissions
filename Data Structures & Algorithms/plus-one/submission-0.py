class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1]+=1
        n = -1
        while digits[n]==10:
            digits[n]=0
            if n==-len(digits):
                digits.insert(0, 1)
                break
            n-=1
            digits[n]+=1
        return digits
