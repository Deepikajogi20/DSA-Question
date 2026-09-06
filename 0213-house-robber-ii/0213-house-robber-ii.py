class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        def rob_linear(houses):
            prev2,prev1=0,0
            for money in houses:
                current=max(prev1,prev2+money)
                prev2=prev1
                prev1=current
            return prev1
        case1=rob_linear(nums[:-1])
        case2=rob_linear(nums[1:])
        return max(case1,case2)