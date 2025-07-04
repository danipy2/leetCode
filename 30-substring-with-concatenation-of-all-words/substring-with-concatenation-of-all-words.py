
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_count = Counter(words)
        num_words = len(words)
        L = len(words[0])
        total_len = L * num_words
        n = len(s)
        ans = []
        
        # Iterate over each alignment modulo L
        for offset in range(L):
            left = offset
            curr = defaultdict(int)
            count = 0
            
            # Slide right in steps of L
            for right in range(offset, n - L + 1, L):
                word = s[right:right + L]
                # If it's one of our target words, include it
                if word in word_count:
                    curr[word] += 1
                    count += 1
                    
                    # If we've exceeded the allowed count,
                    # move `left` forward until we're valid again
                    while curr[word] > word_count[word]:
                        left_word = s[left:left + L]
                        curr[left_word] -= 1
                        left += L
                        count -= 1
                    
                    # If window size hits exactly num_words, record answer
                    if count == num_words:
                        ans.append(left)
                        # Then slide left by one word to look for next possible
                        left_word = s[left:left + L]
                        curr[left_word] -= 1
                        left += L
                        count -= 1
                else:
                    # Reset window if we see a non-matching word
                    curr.clear()
                    count = 0
                    left = right + L
        
        return ans
