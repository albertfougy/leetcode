class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1 or n == 1:
            return 1
        
        #have a list of lists to represent the grid, initilized with 0's
        diffPaths = [[0]*n]*m
        
        #fill row 0 and column 0 with all 1's, only one way to get to all those squares
        for col in range(n):
            diffPaths[0][col] = 1
        
        for row in range(m):
            diffPaths[row][0] = 1
        
        #starting at grid[1][1], go through each gridspace and enter in the amount of unique paths to that square
        #unique paths for a certain square are found by adding the amount of unique paths from each of the squares to its top and its left
        for row in range(1, m):
            for col in range(1, n):
                diffPaths[row][col] = diffPaths[row-1][col] + diffPaths[row][col-1]
        
        #bottom rightmost square will now contain the total amount of unique paths to there
        return diffPaths[m-1][n-1]