class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indices = {}
        for i , n in enumerate(nums):
            if n in indices:
                if abs(indices[n]-i)<=k:
                    return True
                else:
                    indices[n] = i
            if n not in indices:
                indices[n] = i
        return False