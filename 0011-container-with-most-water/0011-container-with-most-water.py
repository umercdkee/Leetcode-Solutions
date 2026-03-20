class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        start = 0
        end = len(height)-1
        while start < end:
            length = end - start
            heights = min(height[start], height[end])
            area = length * heights
            maxArea = max (area, maxArea)
            if height[start]<height[end]:
                start += 1
            else: 
                end -=1
        return maxArea