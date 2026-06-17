class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Basically detecting cycles in Directed Graph. If there is a cycle return False else True
        # Map each course to prereq list
        preMap = { i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # visitset = all courses along the cur DFS path
        visitSet = set()
        def dfs(crs):
            if crs in visitSet:
                return False
            if preMap[crs] == []:
                return True
            
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            # once cycle detection is completed and found safe so we remove and set the crs pre's = []
            visitSet.remove(crs)
            preMap[crs] = []  
            return True

        # This loop for Disconnected graphs (eg: 1 -> 2, 3 -> 4)
        for crs in range(numCourses):
            if not dfs(crs): return False
        
        return True


        

        