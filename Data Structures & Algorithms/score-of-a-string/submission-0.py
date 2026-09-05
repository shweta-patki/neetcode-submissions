class Solution:
    def scoreOfString(self, s: str) -> int:
        ordsum = 0
        for i in range(len(s)-1):
            ordsum += abs(ord(s[i])-ord(s[i+1]))
        return ordsum