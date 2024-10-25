class Solution(object):
    def lengthOfLongestSubstring(self, s):
        maxs = 0
        current_max = 1
        start = 0
        end = 1
        if len(s) > 1:
            while True:
                if end >= len(s):
                    if current_max > maxs:
                        maxs = current_max
                    break
                if s[end] not in s[start:end]:
                        current_max += 1

                else:
                    if current_max > maxs:
                        maxs = current_max
                    current_max = 1
                    start += 1
                    end = start
                end += 1
        else:
            return len(s)
        return maxs