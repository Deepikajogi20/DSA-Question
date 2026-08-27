class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr={}
        for i in range(len(nums)):
            result=target-nums[i]
            if result in arr:
                return [arr[result],i]
            arr[nums[i]]=i