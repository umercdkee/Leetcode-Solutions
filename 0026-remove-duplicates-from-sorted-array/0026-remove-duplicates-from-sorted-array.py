class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        i = 0
        while i<len(nums):
            if i < len(nums)-1 and nums[i] == nums[i+1]:
                nums.pop(i+1)
            else:
                i+=1
                k+=1
        return k