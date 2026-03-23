class Solution:
    def isValid(self, s: str) -> bool:
        lst = []
        i = 0
        opening = '({['
        closing = ')}]'
        while i < len(s):
            if s[i] in opening:
                lst.append(s[i])
            elif s[i] in closing:
                if len(lst) == 0:
                    return False
                elif s[i] == ')' and lst[-1] == '(':
                    lst = lst[:len(lst)-1:]
                elif s[i] == ']' and lst[-1] == '[':
                    lst = lst[:len(lst)-1:]
                elif s[i] == '}' and lst[-1] == '{':
                    lst = lst[:len(lst)-1:]
                else:
                    return False
            i+=1

        if len(lst) == 0:
            return True
        return False