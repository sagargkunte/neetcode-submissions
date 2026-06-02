class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            if matrix[i][0] <= target and matrix[i][col-1] >= target:
                left,right = 0,col-1
                while(left <= right):
                    mid = left + (right-left)//2
                    if matrix[i][mid] == target:
                        return True
                    elif matrix[i][mid] > target:
                        right = mid-1
                    else:
                        left = mid + 1
                return False
        return False
