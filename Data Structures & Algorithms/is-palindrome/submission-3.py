class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_split = s.replace(" ", "").lower()
        s_alphanum = "".join(c for c in s_split if c.isalnum())
        print(math.floor(len(s_alphanum) / 2))
        for c in range (math.floor(len(s_alphanum) / 2)):
            if s_alphanum[c] != s_alphanum[-1 * (c + 1)]:
                return False
        return True