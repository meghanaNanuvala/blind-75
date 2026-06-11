class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # res = []

        # if len(nums) == 1:
        #     return [nums[:]]

        # for i in range(len(nums)):
        #     n = nums.pop(0)

        #     perms = self.permute(nums)
        #     # [2,3], [3,2] -> append 1
        #     for perm in perms:
        #         perm.append(n)
        #     res.extend(perms)
        #     nums.append(n)

        # return res

        res = []

        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for num in nums:
                if num in path:
                    continue

                path.append(num)
                backtrack(path)
                path.pop()

        backtrack([])
        return res

