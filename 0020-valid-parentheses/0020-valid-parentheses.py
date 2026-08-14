class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i]=='(' or s[i]=='[' or s[i]=='{':
                stack.append(s[i])
            elif s[i]==')' or s[i]==']' or s[i]=='}':
                if len(stack) == 0:
                    return False
                top = stack[-1]
                if (s[i]==')' and top!='(') or (s[i]==']' and top!='[') or (s[i]=='}' and top!='{'):
                    return False
                stack.pop()
        if stack:
            return False
        return True