class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return false
        m=len(matrix)
        n=len(matrix[0])
        start=0
        end=m*n-1
        while (start<=end):
            mid=start+(end-start)/2
            row=mid//n
            col=mid%n
            if (matrix[row][col] == target):
                return True
            elif matrix[row][col]>target:
                end=mid-1
            elif matrix[row][col]<target:
                start=mid+1
        
        return False

            
