class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_count = {}
        current_substr = ""
        max_len = 0
        for i in range(len(s)):
            if s[i] not in char_count:
                char_count[s[i]]=len(current_substr)
                current_substr+=s[i]
                if len(current_substr) > max_len:
                    max_len = len (current_substr)
            else:
                to_delete = current_substr[0:char_count[s[i]]+1:1]
                current_substr = current_substr[char_count[s[i]]+1::]
                for j in to_delete:
                    del char_count[j]
                current_substr+=s[i]
                for x in range(len(current_substr)):
                    char_count[current_substr[x]] = x
                
                
                if len(current_substr) > max_len:
                    max_len = len (current_substr)
        return max_len