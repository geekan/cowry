# 注意当板子短的时候就直接算最大长度，就可以O(n)了
class Solution:
    # @return an integer
    def maxArea(self, height):
        length = len(height)
        low = 0
        high = length - 1
        max_area = 0
        while low < high:
            max_area = max(max_area, min(height[low], height[high])*(high-low))
            if height[low] < height[high]:
                low += 1
            else:
                high -= 1
        return max_area

height = [1,5,7,9,10]
print Solution().maxArea(height)