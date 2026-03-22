class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = {}
        s2 = {}
        for c in s:
            if c in s1:
                s1[c]+=1
            else:
                s1[c]=1
        for c in t:
            if c not in s1:
                return False
            if c in s2:
                s2[c]+=1
            else:
                s2[c]=1
        for key, val in s1.items():
            if key not in s2 or val != s2[key]:
                return False
        return True
