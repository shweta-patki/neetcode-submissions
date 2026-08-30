class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'\W', "", s)
        s=s.lower()
        print(s)
        return s==s[::-1]