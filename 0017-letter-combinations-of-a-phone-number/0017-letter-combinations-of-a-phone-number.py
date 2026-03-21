class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combos = [""]
        letters = {"2":"abc",
                   "3": "def",
                   "4": "ghi",
                   "5": "jkl",
                   "6": "mno",
                   "7": "pqrs",
                   "8": "tuv",
                   "9": "wxyz"}
        for num in digits:
            if num == "1":
                pass
            combos = sorted(combos * len(letters[num]))
            for idx, char in enumerate(letters[num]):
                for i in range(idx,len(combos),len(letters[num])):
                    print (combos,i,char)
                    combos[i]+=char
                    #print (combos, num)
                    
        return combos
