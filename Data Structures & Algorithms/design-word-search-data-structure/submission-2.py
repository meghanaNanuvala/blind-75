class WordDictionary:

    def __init__(self):
        self.children = {}
        self.end_of_word = False
        

    def addWord(self, word: str) -> None:
        node = self

        for c in word:
            if c not in node.children:
                node.children[c] = WordDictionary()
            node = node.children[c]
        node.end_of_word = True

    def search(self, word: str) -> bool:

        def dfs(j, node):
            if j == len(word):
                return node.end_of_word

            c = word[j]
            # Running dfs/ backtracking/ recursive on . to find match
            if c == ".":
                for child in node.children.values():
                    if dfs(j+1, child):
                        return True
                return False
            else:
                if c not in node.children:
                    return False
                return dfs(j+1, node.children[c])
                        
        return dfs(0, self)
        
            
