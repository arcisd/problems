# Given two integers n and m, output F_n mod m (that is, the remainder of F_n when divided by m).

import sys

def gcd(a,b):
    if 0 in [a,b] or a==b:
       return max([a,b])
    else: 
       return gcd(min([a,b]),max([a,b])%min([a,b]))

def lcm(a,b):
    if a==0 or b==0:
       return 0
    else:
       return a*b//gcd(a,b)

def pis_period(m):
    F=[0,1] #Fibonacci numbers
    P=[0,1] #Pisano periods
    i=2
    while i!=0:
          F.append(F[i-1]+F[i-2])
          P.append(F[i]%m)
          if P[i-1]==0 and P[i]==1:
             return [i-1,P]
             i=n
          i+=1

def prime_dec(m):
    i=2
    t=m
    D=[1] #Decomposition
    while t!=1:
          if t%i==0:
             t=t//i
             if D[-1]%i==0:
                D[-1]=D[-1]*i
             else:
                D.append(i)
          else:
             i=i+1
    D.pop(0)
    return D

def pis_period_primes(m):
    D=prime_dec(m)
    PS=[]
    for i in D: PS.append(pis_period(i)[0])
    return(PS)

def pis_period_comp(m):
    PS=pis_period_primes(m)
    p=PS[0]
    PS.pop(0)
    for k in PS: p=lcm(p,k)
    return(p)

def calc_fib_faster(n):
    F=[0,1]
    for i in range(2,n+1): F.append(F[i-1]+F[i-2])
    return F[n]

if __name__ == '__main__':
    input=sys.stdin.read();
    n,m=map(int,input.split())
    print(calc_fib_faster(n%pis_period_comp(m))%m)
