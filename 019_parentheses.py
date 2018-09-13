# 019. Find the maximum value of an arithmetic expression by specifying the order of applying its arithmetic operations using additional parentheses.

def evalt(a,b,op):
    if op=='+':
        return a+b
    elif op=='-':
        return a-b
    elif op=='*':
        return a*b
    else:
        assert False

def MinAndMax(i,j,op,m,M):
    mini=float('inf')
    maxi=-float('inf')
    for k in range(i,j):
        a=evalt(M[i][k],M[k+1][j],op[k])
        b=evalt(M[i][k],m[k+1][j],op[k])
        c=evalt(m[i][k],M[k+1][j],op[k])
        d=evalt(m[i][k],m[k+1][j],op[k])
        mini=min(mini,a,b,c,d)
        maxi=max(maxi,a,b,c,d)
    return [mini,maxi]

def get_maximum_value(dataset):
    op=dataset[1:len(dataset):2]
    d=dataset[0:len(dataset)+1:2]
    n=len(d)
    m=[[0]*n for i in range(0,n)]
    M=[[0]*n for i in range(0,n)]
    for i in range(n):
        m[i][i]=int(d[i])
        M[i][i]=int(d[i])
    for s in range(1,n):
        for i in range(0,n-s):
            j=i+s
            m[i][j]=MinAndMax(i,j,op,m,M)[0]
            M[i][j]=MinAndMax(i,j,op,m,M)[1]
    return M[0][n-1]

if __name__=="__main__":
   print(get_maximum_value(input()))
