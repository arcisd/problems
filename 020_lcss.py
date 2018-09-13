# 020. Given three sequences A=(a_1,a_2,...,a_n), B=(b_1,b_2,...,b_m), and C=(c_1,c_2,...,c_l), find the length of their longest common subsequence, i.e., the largest non-negative integer p such that there exist indices 1≤i_1<i_2<···<i_p≤n, 1≤j_1<j_2<···<j_p≤m, 1≤k_1<k_2<···<k_p≤l such that a_{i_1}=b_{j_1}=c_{k_1},...,a_{i_p}=b_{j_p}=c_{k_p}.

import sys

def lcs3(a,b,c):
    matrix=[[[0 for p in range(len(c)+1)] for q in range(len(b)+1)] for r in range(len(a)+1)]
    for i in range(1,len(a)+1):
      for j in range(1,len(b)+1):
          for k in range(1,len(c)+1):
              if a[i-1]==b[j-1]==c[k-1]:
                 matrix[i][j][k]=1+matrix[i-1][j-1][k-1]
              else:
                 matrix[i][j][k]=max(matrix[i][j-1][k],matrix[i-1][j][k],matrix[i][j][k-1])
    return matrix[-1][-1][-1]

def lcs2(a,b):
    matrix=[[0 for p in range(len(b)+1)] for q in range(len(a)+1)]
    for i in range(1,len(a)+1):
      for j in range(1,len(b)+1):
        if a[i-1]==b[j-1]:
          matrix[i][j]=1+matrix[i-1][j-1]
        else:
          matrix[i][j]=max(matrix[i][j-1],matrix[i-1][j])
    return matrix[-1][-1]

if __name__=='__main__':
   input=sys.stdin.read()
   data=list(map(int,input.split()))
   an=data[0]
   data=data[1:]
   a=data[:an]
   data=data[an:]
   bn=data[0]
   data=data[1:]
   b=data[:bn]
   data=data[bn:]
   cn=data[0]
   data=data[1:]
   c=data[:cn]
   print(lcs3(a,b,c))
