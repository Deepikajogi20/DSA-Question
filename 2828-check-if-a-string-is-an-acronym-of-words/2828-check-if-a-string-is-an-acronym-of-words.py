class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        n=len(words)
        j=len(s)
        if n!=j:
            return False

        for i in range(n):
            if words[i][0]!=s[i]:
               return False

        return True