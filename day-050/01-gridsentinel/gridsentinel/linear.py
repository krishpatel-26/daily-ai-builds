
def solve_linear(a, b):
    """Partial-pivot Gaussian elimination. Raises for singular systems."""
    n=len(b)
    if len(a)!=n or any(len(row)!=n for row in a):
        raise ValueError('Expected square matrix')
    if not n:
        return []
    mat=[list(map(float,row))+[float(y)] for row,y in zip(a,b)]
    for k in range(n):
        pivot=max(range(k,n),key=lambda r:abs(mat[r][k]))
        if abs(mat[pivot][k]) < 1e-10:
            raise ValueError('Singular admittance matrix')
        mat[k],mat[pivot]=mat[pivot],mat[k]
        for i in range(k+1,n):
            ratio=mat[i][k]/mat[k][k]
            for j in range(k,n+1):
                mat[i][j]-=ratio*mat[k][j]
    result=[0.0]*n
    for i in reversed(range(n)):
        result[i]=(mat[i][n]-sum(mat[i][j]*result[j] for j in range(i+1,n)))/mat[i][i]
    return result
