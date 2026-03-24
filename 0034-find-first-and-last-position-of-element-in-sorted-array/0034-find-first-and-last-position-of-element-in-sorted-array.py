class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0
        high = len(nums) - 1
        index = -1
        while low <= high and index == -1:
            mid = (low + high) // 2
            if nums[mid] == target:
                index = mid
                break
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        start = index
        end = index
        while start>0 and nums[start] == target:
            if nums[start-1] != target:
                break
            start-=1
        while  end<len(nums)-1 and nums[end] == target :
            if nums[end+1] != target:
                break
            end+=1
        return [start,end]

        