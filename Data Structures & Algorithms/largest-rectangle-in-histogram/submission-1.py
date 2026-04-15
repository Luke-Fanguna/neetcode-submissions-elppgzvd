class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        largestRectangle = 0

        for i in range(len(heights)):
            start_i = i
            # print(i, largestRectangle, stack)
            while stack and stack[-1][1] > heights[i]:
                start, height = stack.pop()
                largestRectangle = max(largestRectangle, (i-start) * height)
                start_i = start
            stack.append((start_i, heights[i]))

        for pos, h in stack:
            largestRectangle = max((len(heights)-pos)*h, largestRectangle)
        
        return largestRectangle

        # for each height,
        # check if the current rectangle extends other rectangles.
        # if not, remove from stack
        # once finished, calculate the rest of the areas with the remaining stack.



#   #
#   #
#   #
#   #     #
#   #     #
#   # # # # 
# # # # # # 