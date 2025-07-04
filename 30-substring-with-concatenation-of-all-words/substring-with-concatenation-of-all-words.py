class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        word_count = Counter(words)
        lgth = len(words[0])
        tlgth = lgth*len(words)
        ans = []
        for i in range(len(s)-tlgth+1):
            copy = defaultdict(int)
            dest = i+tlgth
            if dest  > len(s):
                break
            for j in range(i,dest,lgth):
                word = s[j:j+lgth]
                if word in word_count:
                    copy[word] +=1
                    if copy[word] > word_count[word]:
                        break 
                else:
                    break
            else:
                ans.append(i)
        return ans