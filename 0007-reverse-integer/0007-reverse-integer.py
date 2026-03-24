class Solution:
    def reverse(self, x: int) -> int:
        num = 0
        neg = True if x < 0 else False
        x = abs(x)
        while x != 0:
            if -2**31 <= num * 10 + x % 10 <= (2**31 -1):
                num = num * 10 + x % 10
                x = x // 10
                print (num, x)
            else:
                return 0
        if neg:
            if -2**31 <= num * -1 <= (2**31 -1):
                return num * -1
            else:
                return 0
        return num
            
            