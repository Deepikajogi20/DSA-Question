class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        memo = {}
        return self.backtrack(s, 0, word_set, memo)

    def backtrack(self, s, start, word_set, memo):
        if start == len(s):
            return [""]
        if start in memo:
            return memo[start]

        result = []
        for end in range(start + 1, len(s) + 1):
            word = s[start:end]
            if word in word_set:
                remaining = self.backtrack(s, end, word_set, memo)
                for sentence in remaining:
                    if sentence == "":
                        result.append(word)
                    else:
                        result.append(word + " " + sentence)

        memo[start] = result
        return result