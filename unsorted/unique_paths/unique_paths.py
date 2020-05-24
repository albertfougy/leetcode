class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        #### DP solution ####
        
        # edge cases
        if m <= 0 or n <= 0:
            return 0
        if m == 1 or n == 1:
            return 1
        
        # build an empty matrix
        matrix = [[1 for j in range(n)]for i in range(m)]
        print(matrix)
        
        # record steps for each cell using DP (Expect the first row and the 
        # first column, since there are only one way to get the cells in these places..)
        for i in range(1,m):
            for j in range(1,n):
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
        # accessing the bottom right cell in the grid which contains the unique 
        # number of paths to get to that cell, which is the answer
        return matrix[-1][-1]

