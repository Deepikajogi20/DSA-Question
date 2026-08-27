class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        arr=0
        for i in range(1,len(nums)):
            if nums[arr]!=nums[i]:
                arr+=1
                nums[arr]=nums[i]
        return arr+1  