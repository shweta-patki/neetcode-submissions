class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted([c for c in s])==sorted([c for c in t]):
            return True
        return False