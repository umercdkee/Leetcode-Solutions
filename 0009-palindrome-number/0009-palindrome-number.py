class Solution:
    def isPalindrome(self, x: int) -> bool: 
        if x<0:
            return False
        y = 0
        num = x
        while x > 0:
            y = y * 10 + x % 10
            x = x // 10
            print (y)
        if num == y:
            return True
        return False
        