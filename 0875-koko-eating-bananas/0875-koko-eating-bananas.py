class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low,high=1,max(piles)
        def hours_needed(k):
            return sum(math.ceil(p/k) for p in piles)
        while low<high:
            mid=(low+high)//2
            if hours_needed(mid)<=h:
                high=mid
            else:
                low=mid+1
        return low