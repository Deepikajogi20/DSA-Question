from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        count=Counter(s)
        n=len(s)
        max_freq=max(count.values())
        if max_freq>(n+1)//2:
            return ""
        max_heap=[(-freq,char) for char,freq in count.items()]
        heapq.heapify(max_heap)
        result=[]
        prev_freq,prev_char=0,""
        while max_heap:
            freq,char=heapq.heappop(max_heap)
            result.append(char)
            if prev_freq<0:
                heapq.heappush(max_heap,(prev_freq,prev_char))
            prev_freq,prev_char=freq+1, char
        return "".join(result)