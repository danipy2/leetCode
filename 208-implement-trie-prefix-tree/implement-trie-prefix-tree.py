class TrieNode:
    def __init__(self):
        self.isend = False
        self.word = {}
class Trie:

    def __init__(self):
        self.root = TrieNode()
    def insert(self, word: str) -> None:
        curr = self.root
        for i in word:
            
            if i not in curr.word:
                curr.word[i] = TrieNode()
            curr = curr.word[i]
        curr.isend=True

    def search(self, word: str) -> bool:
        curr = self.root
        for i in word:
            if i not in curr.word:
                return False
            curr = curr.word[i]
        if curr.isend == False:
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for i in prefix:
            ind = ord(i)-ord("a")
            if i not in curr.word:
                return False
            curr = curr.word[i]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)