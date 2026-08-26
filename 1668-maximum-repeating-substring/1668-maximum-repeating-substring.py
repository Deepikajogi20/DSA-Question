class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        k=0
        repeated_word=""
        while (repeated_word+word) in sequence:
            repeated_word+=word
            k+=1
        return k