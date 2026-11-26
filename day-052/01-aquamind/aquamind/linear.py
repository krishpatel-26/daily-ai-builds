"""Dependency-free Gaussian elimination with partial pivoting."""

def solve(matrix, vector):
    n=len(vector)
    if len(matrix)!=n or any(len(row)!=n for row in matrix):
        raise ValueError('Matrix must be square and match vector')
    a=[list(map(float,row))+[float(v)] for row,v in zip(matrix,vector)]
    for col in range(n):
        pivot=max(range(col,n),key=lambda r:abs(a[r][col]))
        if abs(a[pivot][col])<1e-11:raise ValueError('Singular network matrix')
        a[col],a[pivot]=a[pivot],a[col]
        for row in range(col+1,n):
            factor=a[row][col]/a[col][col]
            if factor:
                for j in range(col,n+1):a[row][j]-=factor*a[col][j]
    x=[0.0]*n
    for i in range(n-1,-1,-1):
        x[i]=(a[i][n]-sum(a[i][j]*x[j] for j in range(i+1,n)))/a[i][i]
    return x
