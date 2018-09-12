# Given two integers n and m, output F_n mod m (that is, the remainder of F_n when divided by m).

import sys

def fib_period(n,m):
    F,P,i,p,q,r=[0,1],[0,1],2,0,n,1
    while i<=n:
          F.append(F[i-1]+F[i-2])
          P.append(F[i]%m)
          if P[i-1]==0 and P[i]==1:
             p,q,r,i=i-2,i-1,i-1,n
          i+=1
    return [F[q],p,F[n%r]]

if __name__=='__main__':
   input=sys.stdin.read();
   n,m=map(int,input.split())
   a=fib_period(n,m)
   if a[1]==0:
      print(a[0]%m)
   else:
      print(a[2]%m)

