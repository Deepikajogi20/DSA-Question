class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        for length in range(n - 1, 0, -1):     # try lengths n-1 down to 1
            if s[:length] == s[-length:]:       # prefix == suffix?
                return s[:length]
        return ""
