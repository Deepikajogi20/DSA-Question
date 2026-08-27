class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return 
        word_len=len(words[0])
        total_len=word_len*len(words)
        result=[]
        word_count=Counter(words)
        for i in range(len(s)-total_len+1):
            substring=s[i:i+total_len]
            seen=[]
            for j in range(0,total_len,word_len):
                seen.append(substring[j:j+word_len])
            if Counter(seen)==word_count:
                result.append(i)
        return result