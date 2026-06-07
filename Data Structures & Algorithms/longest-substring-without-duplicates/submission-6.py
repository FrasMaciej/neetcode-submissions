class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars_in_substr = set()
        max_substr_len = 0

        for i, c in enumerate(s):
            chars_in_substr.add(c)
            j = i + 1
            while j <= len(s) - 1:
                if s[j] in chars_in_substr:
                    break
                else:
                    chars_in_substr.add(s[j])
                j += 1
            max_substr_len = max(max_substr_len, len(chars_in_substr))
            chars_in_substr = set()
        if(len(s)) == 1:
            max_substr_len = 1
        return max_substr_len
        