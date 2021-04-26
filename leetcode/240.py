class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            for col in row:
                if col == target:
                    return True
                elif col > target:
                    break
        return False

"""
2중 for문으로 target 보다 작은 수에 대해서만 탐색을 진행하고 없으면 False를 반환했다.
"""