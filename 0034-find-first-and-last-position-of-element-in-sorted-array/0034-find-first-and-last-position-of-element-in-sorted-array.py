class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findIndex(isFirst):
            left = 0
            right = len(nums)-1
            index = -1
            while left<=right:
                mid=(left+right)//2
                if nums[mid]<target:
                    left=mid+1
                elif nums[mid]>target:
                    right=mid-1
                else:
                    index=mid
                    if isFirst:
                       right=mid-1
                    else:
                       left=mid+1
            return index
        first=findIndex(True)
        last=findIndex(False)
        return[first,last]