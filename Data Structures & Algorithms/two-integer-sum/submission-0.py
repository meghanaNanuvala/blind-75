class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}

        for i, num in enumerate(nums):
            y = target - num
            if y in hm:
                return [hm[y], i]
            hm[num] = i

        return []
        

        