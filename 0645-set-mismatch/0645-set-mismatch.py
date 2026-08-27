from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        seen = [0] * (n + 1)
        duplicate = -1
        
        for num in nums:
            seen[num] += 1
            if seen[num] == 2:
                duplicate = num
        
        missing = -1
        for i in range(1, n + 1):
            if seen[i] == 0:
                missing = i
                break
        
        return [duplicate, missing]