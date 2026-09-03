class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in ('(', '{', '['):
                stack.append(i)
            elif stack==[]:
                return False
            elif i==')':
                if stack.pop()=='(':
                    continue
                else:
                    return False
            elif i=='}':
                if stack.pop()=='{':
                    continue
                else:
                    return False
            elif i==']':
                if stack.pop()=='[':
                    continue
                else:
                    return False
        if len(stack)==0:
            return True
        return False