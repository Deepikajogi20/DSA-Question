class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max=nums[0]
        curr_min=nums[0]
        temp=nums[0]
        for i in range(1,len(nums)):
            num=nums[i]
            curr_sum=(num,curr_max*num,curr_min*num)
            curr_max=max(curr_sum)
            curr_min=min(curr_sum)
            temp=max(temp,curr_max)
        return temp