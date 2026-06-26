class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        for i in range(len(s)):
            most_frequent_count = 0
            char_count = {} 
            for j in range(i, len(s)):
                cur_char_count = 1 + char_count.get(s[j], 0)
                char_count[s[j]] = cur_char_count
                most_frequent_count = max(most_frequent_count, cur_char_count)
                substring_length = j - i + 1
                if substring_length - most_frequent_count <= k:
                    res = max(res, substring_length)

        return res 