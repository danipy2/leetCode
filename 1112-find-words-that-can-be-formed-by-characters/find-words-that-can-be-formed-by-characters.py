class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        arr = []
        count = 0
        for word in words:
            arr.append(Counter(word))
        char = Counter(chars)
        for ind,mdict in enumerate(arr):
            for key,value in mdict.items():
               if char.get(key,0) < mdict[key]:
                break
            else:
                count += len(words[ind])
        return count