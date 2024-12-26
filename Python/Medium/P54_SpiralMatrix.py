from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        # Rows
        m = len(matrix)

        # Cols
        n = len(matrix[0])

        totalNums = m * n

        ans = []

        i, j = 0, 0

        UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3

        direction = RIGHT

        UP_WALL = 0
        RIGHT_WALL = n
        DOWN_WALL = m
        LEFT_WALL = -1

        while len(ans) != totalNums:

            if direction == RIGHT:
                while j < RIGHT_WALL:
                    ans.append(matrix[i][j])
                    j += 1
                i, j = i + 1, j - 1
                RIGHT_WALL -= 1
                direction = DOWN

            elif direction == DOWN:
                while i < DOWN_WALL:
                    ans.append(matrix[i][j])
                    i += 1
                i, j = i - 1, j - 1
                DOWN_WALL -= 1
                direction = LEFT

            elif direction == LEFT:
                while j > LEFT_WALL:
                    ans.append(matrix[i][j])
                    j -= 1
                i, j = i - 1, j + 1
                LEFT_WALL += 1
                direction = UP

            else:
                while i > UP_WALL:
                    ans.append(matrix[i][j])
                    i -= 1
                i, j = i + 1, j + 1
                UP_WALL += 1
                direction = RIGHT

        return ans


s = Solution()
print(s.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
