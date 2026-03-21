class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        i = len(s) - 1
        number_dict = {"M": 1000, "D": 500, "C": 100,
                        "L": 50, "X": 10, "V": 5, "I": 1}
        s = s.replace("IV", "IIII")
        s = s.replace("IX", "VIIII")
        s = s.replace("XL", "XXXX")
        s = s.replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC")
        s = s.replace("CM", "DCCCC")
        for char in s:
            num += number_dict[char]
        return num

        