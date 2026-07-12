class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Tricky DP -> from recursion -> True DP
        LIS = [1] * len(nums)
        LIS[len(nums) - 1] = 1


        for i in range(len(nums) - 2, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        
        return max(LIS)

        # O(n^2), O(nlogn)

        

