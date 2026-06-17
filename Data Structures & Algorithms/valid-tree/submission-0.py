class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Empty graph considered as Valid tree
        if not n:
            return True

        adj = { i:[] for i in range(n) }
        
        # since it is a undirected graph
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = set()
        def dfs(i, prev):
            if i in visit:
                return False

            visit.add(i)
            for j in adj[i]:
                if j == prev:
                    continue
                if not dfs(j, i): return False
            
            return True

        # no cycle + every node is connected -> Valid Tree
        return dfs(0, -1) and n == len(visit)

        

