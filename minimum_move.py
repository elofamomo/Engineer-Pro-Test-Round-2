from collections import deque
from typing import List, Tuple
from collections import deque
from collections import defaultdict


class Solution:
    def minimumMoves(self, nums: List[List[int]]) -> int:
        mp = defaultdict(int)
        q = deque()
        q.append((0, 1, 0))
        mp[(0, 1, 0)] += 1
        l = 0
        n = len(nums)

        while q:
            s = len(q)
            while s > 0:
                t = q.popleft()
                i, j, direction = t[0], t[1], t[2]

                if i == n - 1 and j == n - 1 and direction == 0:
                    return l

                if direction == 0:
                    if j + 1 < n and nums[i][j + 1] == 0 and (i, j + 1, 0) not in mp:
                        mp[(i, j + 1, 0)] += 1
                        q.append((i, j + 1, 0))

                    if i + 1 < n and nums[i + 1][j] == 0 and nums[i + 1][j - 1] == 0:
                        if (i + 1, j, 0) not in mp:
                            mp[(i + 1, j, 0)] += 1
                            q.append((i + 1, j, 0))

                        if (i + 1, j - 1, 1) not in mp:
                            mp[(i + 1, j - 1, 1)] += 1
                            q.append((i + 1, j - 1, 1))

                else:
                    if i + 1 < n and nums[i + 1][j] == 0 and (i + 1, j, 1) not in mp:
                        mp[(i + 1, j, 1)] += 1
                        q.append((i + 1, j, 1))

                    if j + 1 < n and nums[i][j + 1] == 0 and nums[i - 1][j + 1] == 0:
                        if (i, j + 1, 1) not in mp:
                            mp[(i, j + 1, 1)] += 1
                            q.append((i, j + 1, 1))

                        if (i - 1, j + 1, 0) not in mp:
                            mp[(i - 1, j + 1, 0)] += 1
                            q.append((i - 1, j + 1, 0))

                s -= 1

            l += 1

        return -1


solution = Solution()
print(solution.minimumMoves([[0, 0, 0, 0, 0, 1],
                             [1, 1, 0, 0, 1, 0],
                             [0, 0, 0, 0, 1, 1],
                             [0, 0, 1, 0, 1, 0],
                             [0, 1, 1, 0, 0, 0],
                             [0, 1, 1, 0, 0, 0]]))
