class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # res = []

        # def backtrack(index, path):
        #     if index == len(nums):
        #         res.append(path[:])
        #         return

        #     path.append(nums[index])
        #     backtrack(index+1, path)
        #     path.pop()

        #     backtrack(index+1, path)

        # backtrack(0, [])
        # return res

        res = []

        subset = []
        def dfs(index):
            if index >= len(nums):
                res.append(subset[:])
                return

            # decision to include nums[index]
            subset.append(nums[index])
            dfs(index + 1) # run dfs recusively on next index

            # decision NOT to include nums[index]
            subset.pop()
            dfs(index + 1)
        
        dfs(0)
        return res
        