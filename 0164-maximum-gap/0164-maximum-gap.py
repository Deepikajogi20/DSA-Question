class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        max_gap=0
        sort_nums=sorted(nums)
        if len(sort_nums)<=1:
            return 0
        for i in range(len(sort_nums)):
            max_gap=max(max_gap,sort_nums[i]-sort_nums[i-1])
        return max_gap