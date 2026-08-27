class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        n=len(nums)
        sort_nums=sorted(nums)
        res=[0]*n
        left=(n-1)//2
        right=n-1
        for i in range(n):
            if i%2==0:
                res[i]=sort_nums[left]
                left-=1
            else:
                res[i]=sort_nums[right]
                right-=1
        nums[:]=res        