class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        def sqn(n):
            sumn = (n%10)**2
            while n:=n//10:
                sumn+=(n%10)**2
            return sumn
        while n!=1:
            if n in seen:
                return False
            seen.add(n)
            n = sqn(n)
        return True