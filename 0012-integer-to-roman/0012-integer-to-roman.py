class Solution:
    def intToRoman(self, num: int) -> str:
        s = ""
        if num >= 1000:
            thousands = num // 1000
            num = num % 1000
            s += "M" * thousands
        if num >=400:
            D = num // 100
            if D == 4:
                s = s+"CD" 
            elif D == 9:
                s = s + "CM"
            else: 
                s = s+"D" + "C" * (D - 5)
            num = num % 100
        elif num >= 100:
            C = num // 100
            s =s + "C" * C
            num = num % 100
        if num >=40:
            D = num // 10
            if D == 4:
                s = s + "XL" 
            elif D == 9:
                s = s + "XC"
            else: 
                s = s+  "L" + "X" * (D - 5)
            num = num % 10
        elif num >= 10:
            C = num // 10
            s = s + "X" * C 
            num = num % 10
        if num >= 4:
            D = num // 1
            if D == 4:
                s = s + "IV"
            elif D == 9:
                s = s + "IX"
            else: 
                s = s + "V" + "I" * (D - 5)
            num = num % 1
        elif num >= 1:
            C = num // 1
            s = s + "I" * C
            num = num % 1
        return s
        