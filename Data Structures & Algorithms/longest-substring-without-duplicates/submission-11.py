class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastSeen = {}
        p1 = 0
        p2 = 0
        maxl = 0
        maxs = ""
        while p2<len(s):
            if s[p2] in lastSeen and lastSeen[s[p2]] >= p1:
                p1 = lastSeen[s[p2]]+1
            lastSeen[s[p2]] = p2
            if p2-p1+1>maxl:
                maxl = p2-p1+1
                maxs = s[p1:p2+1]
            p2+=1
        return maxl