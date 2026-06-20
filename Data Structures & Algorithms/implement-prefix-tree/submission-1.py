class PrefixTree:

    def __init__(self):
        self.children = {}
        self.end_of_word = False
        

    def insert(self, word: str) -> None:
        node = self
        for c in word:
            if c not in node.children:
                node.children[c] = PrefixTree()
            node = node.children[c]

        node.end_of_word = True
            

    def search(self, word: str) -> bool:
        node = self
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.end_of_word
        

    def startsWith(self, prefix: str) -> bool:
        node = self
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True
        
        