class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        min_len = min(strs, key = len)
        for i in range (len(min_len)):
            for j in range (len(strs)):
                if i>=len(strs[j]):
                    return prefix
                if j == 0:
                    prefix+=strs[j][i]
                if strs[j][i] != prefix[-1]:
                    return prefix[:-1:]
        return prefix