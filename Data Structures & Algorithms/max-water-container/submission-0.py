class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Brute Force
        # max_water = float('-inf')

        # for l in range(len(heights)):
        #     for r in range(l+1, len(heights)):
        #         cur_water = min(heights[l], heights[r]) * (r-l)

        #         max_water = max(max_water, cur_water)
            
        # return max_water

        max_water = float('-inf')
        l, r = 0, len(heights)-1

        while l < r:
            cur_water = min(heights[l], heights[r]) * (r-l)
            max_water = max(max_water, cur_water)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_water

            
