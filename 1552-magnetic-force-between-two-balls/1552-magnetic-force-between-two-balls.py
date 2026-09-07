class Solution:
    def maxDistance(self, position, m):
        position.sort()
        
        def can_place(d):
            count = 1  # place first ball at position[0]
            last_pos = position[0]
            for p in position[1:]:
                if p - last_pos >= d:
                    count += 1
                    last_pos = p
                    if count >= m:
                        return True
            return count >= m
        
        left, right = 1, position[-1] - position[0]
        answer = 0
        
        while left <= right:
            mid = (left + right) // 2
            if can_place(mid):
                answer = mid
                left = mid + 1   # try for a bigger minimum distance
            else:
                right = mid - 1  # too far apart, shrink
        
        return answer