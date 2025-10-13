class TrieNode:
    def __init__(self):
        self.isend = False
        self.word = [None for _ in range(26)]
class Trie:

    def __init__(self):
        self.root = TrieNode()
    def insert(self, word: str) -> None:
        curr = self.root
        for i in word:
            ind = ord(i)-ord("a")
            if curr.word[ind]==None:
                curr.word[ind] = TrieNode()
            curr = curr.word[ind]
        curr.isend=True

    def search(self, word: str) -> bool:
        curr = self.root
        for i in word:
            ind = ord(i)-ord("a")
            if curr.word[ind]==None:
                return False
            curr = curr.word[ind]
        if curr.isend == False:
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for i in prefix:
            ind = ord(i)-ord("a")
            if curr.word[ind]==None:
                return False
            curr = curr.word[ind]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)