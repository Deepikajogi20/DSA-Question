class Solution:
    def countOdds(self, low: int, high: int) -> int:
        total = high - low + 1
        if low % 2 != 0 or high % 2 != 0:
            return (total + 1) // 2
        return total // 2