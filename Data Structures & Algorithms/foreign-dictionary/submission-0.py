class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # Initialize adjacency list for all unique characters
        adj = { c:set() for w in words for c in w }


        # Build dependency graph
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))

            # If prefix of 2 words are same & w1 > w2 (Invalid case) 
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""

            # Find the 1st mismatching character
            for j in range(minLen):
                # if letters aren't same
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        # print(adj)
                
        # Post-order DFS with 3-state cycle detection
        # None = unvisited, True = visiting (current_path), False = visited 
        visit = {} 
        res = []

        def dfs(c):
            if c in visit:
                return visit[c] # Returns True if cycle detected, False if already processed
            
            visit[c] = True     # Mark as visiting

            for nei in adj[c]:
                if dfs(nei):
                    return True # Cycle detected down the path

            visit[c] = False # Mark as fully visited
            res.append(c)
            return False

        # Call DFS for all characters
        for c in adj:
            if dfs(c):
                return ""  # Return empty str if cycle is found

        res.reverse()
        return ''.join(res)