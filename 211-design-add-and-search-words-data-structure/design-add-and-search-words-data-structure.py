class TrieNode:
    def __init__(self):
        self.isend = False
        self.c = {}

class WordDictionary:
    
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for i in word:
            if i not in curr.c:
                curr.c[i] = TrieNode()
            curr = curr.c[i]
        curr.isend = True
        
    def search(self, word: str,curr:TrieNode = None) -> bool:
        if curr == None:
            curr = self.root
        
        for k in range(len(word)):
            i = word[k]
            if i ==".":
                for j in curr.c:
                    if self.search(word[k+1:],curr.c[j]):
                        return True
                return False
            if i in curr.c:
                curr = curr.c[i]
            else:
                return False
        return curr.isend



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)