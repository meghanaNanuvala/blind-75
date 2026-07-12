class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1

        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue
            
            #[-1, 8] #[-1, -8]
            curMax, curMin = max(n * curMax, n * curMin, n), min(n * curMax, n * curMin, n) 

            res = max(res, curMax)
        return res

        # O(n), O(1)



