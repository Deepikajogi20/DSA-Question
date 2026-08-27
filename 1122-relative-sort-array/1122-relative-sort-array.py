class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1=arr1[:]
        result=[]
        for num in arr2:
            i=0
            while i<len(arr1):
                if arr1[i]==num:
                    result.append(arr1[i])
                    arr1.pop(i)
                else:
                    i+=1
        arr1.sort()
        result.extend(arr1)
        return result