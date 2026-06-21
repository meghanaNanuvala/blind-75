class TrieNode:
    def __init__(self):
            self.children = {}
            self.end_of_word = False

    def addWord(self, word):
        node = self

        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]

        node.end_of_word = True        

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        node = TrieNode()

        for w in words:
            node.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS
            or (r,c) in visit or board[r][c] not in node.children):
                return

            visit.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]

            if node.end_of_word:
                res.add(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            visit.remove((r,c)) # backtracking from the path

    
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, node, '')
        

        return list(res)
            
        

            

            
                

