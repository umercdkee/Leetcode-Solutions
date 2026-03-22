class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for i in nums:
            if i in count:
                return True
            if i not in count:
                count[i] = 1
        return False