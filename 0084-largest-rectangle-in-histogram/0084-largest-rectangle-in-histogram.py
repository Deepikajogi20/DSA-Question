class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        maxarea=0
        n=len(heights)
        for i in range(len(heights)):
            while stack and heights[stack[-1]]>heights[i]:
                h=heights[stack.pop()]
                if stack:
                    width=i-stack[-1]-1
                else:
                    width=i
                area=h*width
                if area>maxarea:
                    maxarea=area
            stack.append(i)
        while stack:
            h=heights[stack.pop()]
            if stack:
                width=n-stack[-1]-1
            else:
                width=n
            area=h*width
            if area>maxarea:
                maxarea=area
        return maxarea