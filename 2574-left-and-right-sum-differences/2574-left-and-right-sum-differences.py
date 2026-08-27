class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        arr=[]
        leftsum=0
        total=sum(nums)
        for i in nums:
            rightsum=total-leftsum-i
            arr.append(abs(leftsum-rightsum))
            leftsum+=i
        return arr