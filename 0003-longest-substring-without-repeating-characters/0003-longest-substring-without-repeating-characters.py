class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=set()
        left=0
        max_len=0
        for i in range(len(s)):
            while s[i] in n:
                n.remove(s[left])
                left+=1
            n.add(s[i])
            max_len=max(max_len,i-left+1)
        return max_len