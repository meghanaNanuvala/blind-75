class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # res = []

        # def dfs(index, path, total):
        #     if total == target:
        #         res.append(path[:])
        #         return

            
        #     if index >= len(nums) or total > target:
        #         return

        #     # decision to include nums[index] on left
        #     path.append(nums[index])
        #     dfs(index, path, total + nums[index])  # running dfs recursively on duplicates

        #     # decision NOT to include nums[index] on right
        #     path.pop()
        #     dfs(index + 1, path, total)

        # dfs(0, [], 0)
        # return res

        res = []

        def backtrack(start, path, target):
            if target == 0:
                res.append(path[:])
                return

            if target < 0:
                return

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i, path, target - nums[i])
                path.pop()

        backtrack(0, [], target)
        return res



