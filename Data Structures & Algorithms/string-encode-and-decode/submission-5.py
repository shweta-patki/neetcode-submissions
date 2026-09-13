class Solution:

    def encode(self, strs: List[str]) -> str:
        strj = ""
        for i in strs:
            strj += str(len(i))+'#'+i
        return strj

    def decode(self, s: str) -> List[str]:
        l = []
        ch=0
        while ch in range(len(s)):
            print(s[ch])
            le = ''
            while s[ch]!='#':
                le+=s[ch]
                ch+=1
            ch+=1
            l.append(s[ch:ch+int(le)])
            ch+=int(le)
        return l