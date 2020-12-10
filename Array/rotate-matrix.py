class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
        n  = len(A)
        for i in range(n):
            for j in range(i):
                A[i][j],A[j][i] = A[j][i],A[i][j]
        for i in range(n):
            for j in range(n//2):
                A[i][j],A[i][n-j-1] = A[i][n-j-1],A[i][j]
        return A
                