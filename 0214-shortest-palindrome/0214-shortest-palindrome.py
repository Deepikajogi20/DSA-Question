class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        n=len(s)
        def is_palindrome(string:str)->bool:
            return string==string[::-1]
        for i in range(n,0,-1):
            if is_palindrome(s[:i]):
                return s[i:][::-1]+s
        return s[1:][::-1]+s
        