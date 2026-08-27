class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        return self.mergeSort(0, len(nums)-1, nums)
    def mergeSort(self, l, r, nums):
        if l >= r:
            return 0
        mid = (l+r)//2
        count = 0
        count += self.mergeSort(l, mid, nums)
        count += self.mergeSort(mid+1,r, nums)
        count += self.merge(l,mid,r, nums)
        return count

    def merge(self, l, mid, r, arr):
        temp = []
        j = mid+1
        
        
        count = 0
        for i in range(l, mid+1):
            while j <=r and arr[i] > 2*arr[j]:
                j += 1
            count += j - (mid+1)

        i = l
        j = mid+1
        while i <= mid and j <= r:
            if arr[i] < arr[j]:
                temp.append(arr[i])
                i+=1
            else:
                temp.append(arr[j])
                j+=1

        while i <= mid:
            temp.append(arr[i])
            i+=1
        while j<=r:
            temp.append(arr[j])
            j+=1
        arr[l:r + 1] = temp
        return count
                

            