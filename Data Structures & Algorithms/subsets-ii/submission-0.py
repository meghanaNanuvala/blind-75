class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        prev = -1

        def backtrack(pos, path):
            if pos == len(nums):
                res.append(path[:])
                return
        

            # explore path that has nums[i]
            path.append(nums[pos])
            backtrack(pos+1, path)
            path.pop()

            # skipping duplicates for the right side tree
            while pos+1 < len(nums) and nums[pos] == nums[pos+1]:
                pos += 1

            # explore path NOT to include nums[i]
            backtrack(pos+1, path)

            
        backtrack(0, [])
        return res