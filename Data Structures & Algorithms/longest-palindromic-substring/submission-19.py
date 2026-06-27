class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.resIdx = 0
        self.resLen = 0
        self.s = s

        for i in range(len(s)):
            self.check_palindrome(i, i)            
            self.check_palindrome(i, i + 1)
  
        return self.s[self.resIdx : self.resIdx + self.resLen]

    def check_palindrome(self, l, r):
        while l >= 0 and r < len(self.s) and self.s[l] == self.s[r]:
            if (r - l + 1) > self.resLen:
                self.resIdx = l
                self.resLen = r - l + 1
            l -= 1
            r += 1