class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_generator={}
        stack=[]
        for num in nums2:
            while stack and stack[-1]<num:
                next_generator[stack.pop()]=num
            stack.append(num)
        return [next_generator.get(n,-1) for n in nums1]