class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ns = ""
        rowCount = 0
        rows=[[] for _ in range (numRows)]
        down = True
        i = 0
        print (rows, s)
        while i < len(s):
            print(rowCount, i)
            rows[rowCount].append(s[i])
            i += 1
            if rowCount>=numRows-1:
                down = False
            elif rowCount <= 0:
                down = True
            if down:
                rowCount += 1
            else: 
                rowCount -= 1

        for row in rows:
            for j in row:
                ns += j
        
        return ns