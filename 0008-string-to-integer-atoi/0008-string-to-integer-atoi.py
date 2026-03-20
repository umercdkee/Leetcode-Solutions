class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        while i < len(s) and s[i] == " ":
            i += 1
        s = s[i::]
        print (s)
        i = 0
        if len(s)==0:
            return 0
        num = 0
        pos = True
        if s[i]=='-':
            pos = False
            i+=1
        elif s[i]=='+':
            i+=1
        while i<len(s):
            if not s[i].isdigit():
                break
            num = num * 10 + int(s[i])
            i+=1
        if not pos:
            num *= -1
        if num > 2**31 -1:
            return 2**31 -1
        elif num < -2**31:
            return -2**31
        return num