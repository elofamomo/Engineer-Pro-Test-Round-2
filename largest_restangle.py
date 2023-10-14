from typing import List


from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        n = len(heights)
        stack = []
        for i in range(n):
            if not stack or heights[i] > heights[stack[-1]]:
                stack.append(i)

            # if i > 0 and  heights[i] == heights[i - 1]:
            #     continue
            # j = i + 1
            # k = i - 1
            # rectangle = heights[i]
            # left = 0
            # right = 0
            # while j < n and heights[j] >= heights[i] :
            #     right += heights[i]
            #     j += 1
            # while k >= 0 and heights[k] >= heights[i]:
            #     left += heights[i]
            #     k -= 1
            # rectangle = rectangle + left + right
            # if rectangle > res:
            #     res = rectangle
        return res

# solution = Solution()
# print(solution.largestRectangleArea([2,1,2]))

# solution = Solution()
# print(solution.largestRectangleArea([2,1,2]))

solution = Solution()
print(solution.largestRectangleArea([2,1,2]))