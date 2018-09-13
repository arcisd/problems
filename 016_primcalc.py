# 016. Given an integer n, compute the minimum number of operations needed to obtain the number n starting from the number 1.

import sys

def numop(n):
    C=[0,0]
    L=[n]
    if n==1:
       return [1]
    for i in range(2,n+1):
        mint=[C[i-1]+1]
        if i%3==0:
           mint.append(C[i//3]+1)
        if i%2==0:
           mint.append(C[i//2]+1)
        C.append(min(mint))
        k=n
    while k>1:
          if k%3==0 and C[k//3]==C[k]-1:
             k=k//3
             L.append(k)
          elif k%2==0 and C[k//2]==C[k]-1:
             k=k//2
             L.append(k)
          else:
             k=k-1
             L.append(k)
    L.reverse()
    return L

input=sys.stdin.read()
n=int(input)
sequence=list(numop(n))
print(len(sequence)-1)
for x in sequence: print(x,end=' ')
