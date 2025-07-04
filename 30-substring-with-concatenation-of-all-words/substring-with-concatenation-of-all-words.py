class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        word_count = Counter(words)
        lgth = len(words[0])
        num_words = len(words)
        tlgth = lgth*num_words
        n = len(s)
        ans = []
        for i in range(lgth):
            left = i
            curr = defaultdict(int)
            count = 0
            for j in range(i,n-lgth+1,lgth):
                word = s[j:j+lgth]
                if word in word_count:
                    curr[word] +=1
                    count+=1
                    while curr[word] > word_count[word]:
                        left_word = s[left:left + lgth]
                        curr[left_word] -= 1
                        left += lgth
                        count -= 1
                    if count == num_words:
                        ans.append(left)
                        left_word = s[left:left + lgth]
                        curr[left_word] -= 1
                        left += lgth
                        count -= 1
                else:
                    curr.clear()
                    count = 0
                    left = j + lgth
        return ans