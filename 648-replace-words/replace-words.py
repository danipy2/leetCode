class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        t = Trie()
        for word in dictionary:
            t.insert(word)
        arr = sentence.split()
        for i in range(len(arr)):
            getword = t.search(arr[i])
            if getword!="":
                arr[i] = getword
        return " ".join(arr)
class TrieNode:
    def __init__(self):
        self.isend = False
        self.children = {}
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,word):
        curr = self.root
        for i in word:
            if i not in curr.children:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.isend = True

    def search(self,word):
        curr = self.root
        for i in range(len(word)):
            w = word[i]
            if w in curr.children:
                curr = curr.children[w]
                if curr.isend:
                    return word[:i+1]
            else:
                return ""
        return word
        


    