class TrieNode:
    def __init__(self):
        self.isend = False
        self.c = {}

class WordDictionary:
    
    def __init__(self):
        self.root = TrieNode()
        self.cond = False

    def addWord(self, word: str) -> None:
        curr = self.root
        for i in word:
            if i not in curr.c:
                curr.c[i] = TrieNode()
            curr = curr.c[i]
        curr.isend = True
        
    def search(self, word: str,curr:TrieNode = None) -> bool:
        if self.cond ==True:
            return True
        if curr == None:
            curr = self.root
            self.cond = False
        for k in range(len(word)):
            i = word[k]
            if i ==".":
                cond = False
                for j in curr.c:
                    cond = cond or self.search(word[k+1:],curr.c[j])
                if cond:
                    return True
                return False
            if i in curr.c:
                curr = curr.c[i]
                continue
            return False
        if curr.isend:
            return True
        return False



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)