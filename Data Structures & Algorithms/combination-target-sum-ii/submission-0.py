class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []

        def backtrack(pos, path, target):
            if target == 0:
                res.append(path[:])
                return

            if target <= 0:
                return

            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue
                path.append(candidates[i])
                backtrack(i + 1, path, target - candidates[i])
                path.pop()
                prev = candidates[i]

        backtrack(0, [], target)
        return res
            
            
        
        