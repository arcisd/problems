# 018. The goal of this problem is to implement the algorithm for computing the edit distance between two strings.

def edit_distance(s,t):
    n=len(s)
    m=len(t)
    matrix =[[0]*(m+1) for k in range(0,n+1)]
    for j in range(0,m+1):matrix[0][j]=j
    for i in range(0,n+1):matrix[i][0]=i
    for i in range (1,n+1):
        for j in range(1,m+1):
            insertion=matrix[i][j-1]+1
            deletion=matrix[i-1][j]+1
            match=matrix[i-1][j-1]
            mismatch=matrix[i-1][j-1]+1
            if s[i-1]==t[j-1]:
               matrix[i][j]=min(insertion,deletion,match)
            else:
               matrix[i][j]=min(insertion,deletion,mismatch)
    return matrix[n][m]

if __name__=="__main__":
   print(edit_distance(input(),input()))
